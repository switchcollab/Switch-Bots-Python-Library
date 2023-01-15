import re
from typing import TYPE_CHECKING, Generic, TypeVar
from switch.bots.constants import VALID_COMMAND_REGEX
from switch.types import EventType

from switch.utils.types import SCT, HandlerCallback
from switch.bots.handlers.base_handler import BaseHandler
from switch.bots.bot_context import BotContext
from switch.api.chat.events import CommandEvent
from switch.api.common.events import Event

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class EventHandler(BaseHandler):
    def __init__(
        self,
        event_types: SCT[EventType],
        callback: HandlerCallback[BotContext[Event], ResType],
        **kwargs,
    ):
        super().__init__(callback, **kwargs)
        if isinstance(event_types, EventType):
            event_types = frozenset({event_types})
        else:
            event_types = frozenset(event_types)
        self.event_types = event_types

    async def should_handle(self, context: BotContext[Event]) -> bool:
        if context.event.type in self.event_types:
            return True
        return False
