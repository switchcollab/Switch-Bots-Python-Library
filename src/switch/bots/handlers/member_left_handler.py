from typing import TYPE_CHECKING, Optional, TypeVar
from switch.api.community.events import MemberLeftEvent
from switch.bots.filters.filter import Filter

from switch.bots import BotContext
from .event_handler import EventHandler
from switch.types import EventType
from switch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class MemberLeftHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[MemberLeftEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.MEMBER_LEAVE, callback, filter, **kwargs)
