import re
from typing import Optional
from swibots.api.chat.events import MessageEvent
from swibots.api.chat.events.chat_event import ChatEvent
from swibots.api.common.events import Event
from swibots.bots.bot_context import BotContext
from swibots.utils.types import SCT, FilterCallback
from swibots.types import EventType
from typing import Callable, Union, List, Pattern


class Filter:
    async def __call__(self, ctx: BotContext) -> bool:
        raise NotImplementedError

    def __invert__(self):
        return InvertFilter(self)

    def __and__(self, other):
        return AndFilter(self, other)

    def __or__(self, other):
        return OrFilter(self, other)


class InvertFilter(Filter):
    def __init__(self, base):
        self.base = base

    async def __call__(self, ctx: BotContext) -> bool:
        result = await self.base(ctx)
        return not result


class AndFilter(Filter):
    def __init__(self, base, other):
        self.base = base
        self.other = other

    async def __call__(self, ctx: BotContext) -> bool:
        r1 = await self.base(ctx)
        # short circuit
        if not r1:
            return False
        r2 = await self.other(ctx)

        return r1 and r2


class OrFilter(Filter):
    def __init__(self, base, other):
        self.base = base
        self.other = other

    async def __call__(self, ctx: BotContext) -> bool:
        r1 = await self.base(ctx)
        # short circuit
        if r1:
            return True

        return await self.other(ctx)


CUSTOM_FILTER_NAME = "CustomFilter"


def create(func: FilterCallback, name: str = None, **kwargs) -> Filter:
    return type(
        name or func.__name__ or CUSTOM_FILTER_NAME,
        (Filter,),
        {"__call__": func, **kwargs},
    )()


async def all_filter(self, ctx: BotContext):
    return True


all = create(all_filter)
"""Filter all messages."""


async def self_filter(self, ctx: BotContext[MessageEvent]):
    return bool(
        ctx.event.message is not None
        and ctx.event.message.user_id == ctx.event.message.receiver_id
    )


self = create(self_filter)
"""Filter messages generated by the same user."""


async def bot_filter(self, ctx: BotContext[MessageEvent]):
    return bool(
        ctx.event.message is not None
        and ctx.event.user is not None
        and ctx.event.user.is_bot
    )


is_bot = create(bot_filter)
"""Filter messages coming from bots."""


async def personal_filter(self, ctx: BotContext[MessageEvent]):
    return ctx.event.message.personal_chat


personal = create(personal_filter)


async def communities_filter(self, ctx: BotContext[MessageEvent]):
    return bool(ctx.event.message.community_id)


communities = create(communities_filter)
channels = create(lambda _, ctx: ctx.event.message.channel_chat)
groups = create(lambda _, ctx: ctx.event.message.group_chat)


async def me_filter(self, ctx: BotContext[MessageEvent]):
    return bool(
        ctx.event.message is not None and ctx.event.message.user_id == ctx.user.id
    )


me = create(me_filter)
"""Filter messages coming from your user."""


async def incoming_filter(self, ctx: BotContext[MessageEvent]):
    return bool(
        ctx.event.message is not None and ctx.event.message.receiver_id == ctx.user.id
    )


incoming = create(incoming_filter)
"""Filter incoming messages. Messages that are sent to the users recipient."""


async def outgoing_filter(self, ctx: BotContext[MessageEvent]):
    return not incoming(ctx)


outgoing = create(outgoing_filter)
"""Filter outgoing messages. Messages that are sent by the user."""


async def admin_filter(self, ctx: BotContext[MessageEvent]):
    m = ctx.event.message
    if not m.community_id:
        return False
    return await ctx.is_admin(m.community_id, m.user_id)


admin = create(admin_filter)


class community(Filter, set):
    """Filter events comming from a specific community or communities"""

    def __init__(self, community_id: Optional[SCT[str]]):
        self.community_id = community_id

    async def __call__(self, ctx: BotContext[Event]):
        community_id = self.community_id
        if community_id is None:
            return bool(ctx.event.community_id is not None)
        if isinstance(community_id, str):
            community_id = frozenset({community_id})
        else:
            community_id = frozenset(community_id)
        return bool(ctx.event.community_id in community_id)


class channel(Filter, set):
    """Filter events comming from a specific channel or channels"""

    def __init__(self, channel_id: Optional[SCT[str]]):
        self.channel_id = channel_id

    async def __call__(self, ctx: BotContext[Event]):
        channel_id = self.channel_id
        if channel_id is None:
            return bool(ctx.event.channel_id is not None)
        if isinstance(channel_id, str):
            channel_id = frozenset({channel_id})
        else:
            channel_id = frozenset(channel_id)
        return bool(ctx.event.channel_id in channel_id)


class group(Filter, set):
    def __init__(self, group_id: Optional[SCT[str]]):
        self.group_id = group_id

    async def __call__(self, ctx: BotContext[Event]):
        group_id = self.group_id
        if group_id is None:
            return ctx.event.group_id is not None
        if isinstance(group_id, str):
            group_id = frozenset({group_id})
        else:
            group_id = frozenset(group_id)
        return bool(ctx.event.group_id in group_id)


class user(Filter, set):
    def __init__(self, user_id: Optional[SCT[int]]):
        self.user_id = user_id

    async def __call__(self, ctx: BotContext[Event]):
        user_id = self.user_id
        if user_id is None:
            return bool(ctx.event.action_by_id is not None)
        if isinstance(user_id, int):
            user_id = frozenset({user_id})
        else:
            user_id = frozenset(user_id)
        return bool(ctx.event.action_by_id in user_id)


def text(text: Optional[SCT[str]]):
    async def func(self, ctx: BotContext[MessageEvent]):
        text = self.text
        if text is None:
            return bool(
                ctx.event.message is not None and ctx.event.message.message is not None
            )
        if isinstance(text, str):
            text = frozenset({text})
        else:
            text = frozenset(text)

        if ctx.event.type == EventType.MESSAGE:
            value = ctx.event.message.message
        elif ctx.event.type == EventType.COMMAND:
            value = ctx.event.command
        elif ctx.event.type == EventType.CALLBACK_QUERY:
            value = ctx.event.callback_data

        for t in text:
            if t in value:
                return True
            else:
                try:
                    regexp = re.compile(t)
                    if regexp.search(value):
                        return True
                except re.error:
                    pass
        return False

    return create(func, name="TextFilter", text=text)


""" Filter messages by text. """


def regexp(regexp: Optional[SCT[str]]):
    async def func(self, ctx: BotContext[MessageEvent]):
        regexp = self.regexp
        if regexp is None:
            return bool(
                ctx.event.message is not None and ctx.event.message.message is not None
            )
        if isinstance(regexp, str):
            regexp = frozenset({regexp})
        else:
            regexp = frozenset(regexp)

        if ctx.event.type == EventType.MESSAGE:
            value = ctx.event.message.message
        elif ctx.event.type == EventType.COMMAND:
            value = ctx.event.command
        elif ctx.event.type == EventType.CALLBACK_QUERY:
            value = ctx.event.callback_data

        if value is None:
            return False

        for r in regexp:
            try:
                cr = re.compile(r)
                if cr.match(value):
                    return True
            except re.error:
                pass
        return False

    return create(func, name="RegexpFilter", regexp=regexp)


""" Filter messages by regexp. """


async def message_type(types: Optional[SCT[int]]):
    async def func(self, ctx: BotContext[MessageEvent]):
        types = self.types
        if types is None:
            return bool(ctx.event.message.status is not None)
        if isinstance(types, int):
            types = frozenset({types})
        else:
            types = frozenset(types)
        return bool(ctx.event.message.status in types)

    return create(func, name="MessageType", types=types)
