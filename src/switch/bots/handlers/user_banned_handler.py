from typing import TYPE_CHECKING, Optional, TypeVar
from switch.api.community.events import UserBannedEvent
from switch.bots.filters.filter import Filter

from switch.bots import BotContext
from .event_handler import EventHandler
from switch.types import EventType
from switch.utils.types import HandlerCallback

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
