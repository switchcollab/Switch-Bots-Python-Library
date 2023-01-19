from typing import TYPE_CHECKING, Optional, TypeVar
from swibots.api.community.events import CommunityUpdatedEvent
from swibots.bots.filters.filter import Filter

from swibots.bots import BotContext
from .event_handler import EventHandler
from swibots.types import EventType
from swibots.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class CommunityUpdatedHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[CommunityUpdatedEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.COMMUNITY_UPDATE, callback, filter, **kwargs)
