from typing import TYPE_CHECKING, TypeVar
from switch.api.chat.events import MessageEvent
from switch.api.community.events import CommunityEvent
from switch.bots.filters.filter import Filter

from switch.bots.handlers import BaseHandler
from switch.bots import BotContext
from .event_handler import EventHandler
from switch.types import EventType
from switch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class ChannelUpdatedHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[CommunityEvent], ResType],
        filter: Filter = None,
        **kwargs,
    ):
        super().__init__(EventType.CHANNEL_UPDATE, callback, filter, **kwargs)
