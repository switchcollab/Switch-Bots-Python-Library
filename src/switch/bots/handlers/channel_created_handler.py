from typing import TYPE_CHECKING, Optional, TypeVar
from switch.api.community.events import ChannelCreatedEvent
from switch.bots.filters import Filter

from switch.bots import BotContext
from .event_handler import EventHandler
from switch.types import EventType
from switch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class ChannelCreatedHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[ChannelCreatedEvent], ResType],
        filter: Optional[Filter],
        **kwargs,
    ):
        super().__init__(EventType.CHANNEL_CREATE, callback, filter, **kwargs)
