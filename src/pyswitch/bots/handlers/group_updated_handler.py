from typing import TYPE_CHECKING, Optional, TypeVar
from pyswitch.api.chat.events import MessageEvent
from pyswitch.api.community.events import GroupUpdatedEvent
from pyswitch.bots.filters.filter import Filter

from pyswitch.bots.handlers import BaseHandler
from pyswitch.bots import BotContext
from .event_handler import EventHandler
from pyswitch.types import EventType
from pyswitch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class GroupUpdatedHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[GroupUpdatedEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.GROUP_UPDATE, callback, filter, **kwargs)
