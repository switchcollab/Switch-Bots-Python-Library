from typing import TYPE_CHECKING, Optional, TypeVar
from pyswitch.api.community.events import UserBannedEvent
from pyswitch.bots.filters.filter import Filter

from pyswitch.bots import BotContext
from .event_handler import EventHandler
from pyswitch.types import EventType
from pyswitch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class UserBannedHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[UserBannedEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.USER_BAN, callback, filter, **kwargs)
