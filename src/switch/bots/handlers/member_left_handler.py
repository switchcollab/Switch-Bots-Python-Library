from typing import TYPE_CHECKING, TypeVar
from switch.api.chat.events import MessageEvent
from switch.api.community.events import CommunityEvent

from switch.bots.handlers import BaseHandler
from switch.bots import BotContext
from .event_handler import EventHandler
from switch.types import EventType
from switch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class MemberLeftHandler(EventHandler):
    def __init__(self, callback: HandlerCallback[BotContext[CommunityEvent], ResType], **kwargs):
        super().__init__(EventType.MEMBER_LEAVE, callback, **kwargs)
