import re
from typing import TYPE_CHECKING, Generic, Optional, TypeVar
from pyswitch.bots.constants import VALID_COMMAND_REGEX
from pyswitch.bots.filters.filter import Filter
from pyswitch.types import EventType

from pyswitch.utils.types import SCT, HandlerCallback
from pyswitch.bots.handlers.base_handler import BaseHandler
from pyswitch.bots.bot_context import BotContext
from pyswitch.api.chat.events import CommandEvent
from pyswitch.api.common.events import Event

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
