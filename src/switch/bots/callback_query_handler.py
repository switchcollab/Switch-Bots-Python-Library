import re
from typing import TYPE_CHECKING, TypeVar
from switch.bots.constants import EventType
from switch.bots.callback_query_event import CallbackQueryEvent

from switch.utils.types import SCT, HandlerCallback
from switch.bots.base_handler import BaseHandler
from switch.bots.bot_context import BotContext
from switch.bots.event import Event

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class CallbackQueryHandler(BaseHandler):
    def __init__(
        self, callback: HandlerCallback[BotContext[CallbackQueryEvent], ResType], **kwargs
    ):
        super().__init__(callback, **kwargs)

    async def should_handle(self, context: BotContext[CallbackQueryEvent]) -> bool:
        if context.event.type == EventType.CALLBACK_QUERY and context.event.message is not None:
            return True
        return False
