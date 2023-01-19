from typing import TYPE_CHECKING, Optional, TypeVar
from pyswitch.api.community.events import GroupCreatedEvent
from pyswitch.bots.filters.filter import Filter

from pyswitch.bots import BotContext
from .event_handler import EventHandler
from pyswitch.types import EventType
from pyswitch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class GroupCreatedHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[GroupCreatedEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.GROUP_CREATE, callback, filter, **kwargs)
