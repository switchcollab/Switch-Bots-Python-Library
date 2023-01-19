from typing import TYPE_CHECKING, Optional, TypeVar
from pyswitch.api.community.events import ChannelCreatedEvent
from pyswitch.bots.filters import Filter

from pyswitch.bots import BotContext
from .event_handler import EventHandler
from pyswitch.types import EventType
from pyswitch.utils.types import HandlerCallback

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
