from typing import TYPE_CHECKING, Optional, TypeVar
from switch.api.chat.events import MessageEvent
from switch.api.community.events import CommunityEvent
from switch.bots.filters import Filter

from switch.bots.handlers import BaseHandler
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
        callback: HandlerCallback[BotContext[CommunityEvent], ResType],
        filter: Optional[Filter],
        **kwargs,
    ):
        super().__init__(EventType.CHANNEL_CREATE, callback, filter, **kwargs)
