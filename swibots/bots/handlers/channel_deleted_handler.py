from typing import TYPE_CHECKING, Optional, TypeVar
from swibots.api.community.events import ChannelDeletedEvent
from swibots.bots.filters.filter import Filter

from swibots.bots import BotContext
from .event_handler import EventHandler
from swibots.types import EventType
from swibots.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class ChannelDeletedHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[ChannelDeletedEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.COMMUNITY_CHANNEL_DELETE, callback, filter, **kwargs)
