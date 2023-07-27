import re
from typing import TYPE_CHECKING, Generic, Optional, TypeVar
from swibots.bots.constants import VALID_COMMAND_REGEX
from swibots.bots.filters.filter import Filter
from swibots.types import EventType

from swibots.utils.types import SCT, HandlerCallback
from swibots.bots.handlers.base_handler import BaseHandler
from swibots.bots.bot_context import BotContext
from swibots.api.chat.events import CommandEvent
from swibots.api.common.events import Event

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class EventHandler(BaseHandler):
    def __init__(
        self,
        event_types: Optional[SCT[EventType]],
        callback: HandlerCallback[BotContext[Event], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(callback, filter, **kwargs)
        if isinstance(event_types, EventType):
            event_types = frozenset({event_types})
        else:
            event_types = frozenset(event_types)
        self.event_types = event_types
        self.filter = filter

    async def should_handle(self, context: BotContext[Event]) -> bool:
        if (self.event_types is not None) and (not context.event.type in self.event_types):
            return False
        if self.filter:
            return await self.filter(context)
        return True
