import re
from typing import TYPE_CHECKING, TypeVar
from switch.bots.constants import EventType
from switch.bots.message_event import MessageEvent

from switch.utils.types import SCT, HandlerCallback
from switch.bots.base_handler import BaseHandler
from switch.bots.bot_context import BotContext
from switch.bots.event import Event

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class MessageHandler(BaseHandler):
    def __init__(self, callback: HandlerCallback[BotContext[MessageEvent], ResType], **kwargs):
        super().__init__(callback, **kwargs)

    async def should_handle(self, context: BotContext[MessageEvent]) -> bool:
        if context.event.type == EventType.MESSAGE and context.event.message is not None:
            return True
        return False
