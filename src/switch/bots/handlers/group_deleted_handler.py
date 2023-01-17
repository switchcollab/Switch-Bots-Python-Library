from typing import TYPE_CHECKING, Optional, TypeVar
from switch.api.chat.events import MessageEvent
from switch.api.community.events import GroupDeletedEvent
from switch.bots.filters.filter import Filter

from switch.bots.handlers import BaseHandler
from switch.bots import BotContext
from .event_handler import EventHandler
from switch.types import EventType
from switch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class GroupDeletedHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[GroupDeletedEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.GROUP_DELETE, callback, filter, **kwargs)