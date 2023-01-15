import re
from typing import TYPE_CHECKING, TypeVar
from switch.api.chat.events import CallbackQueryEvent
from switch.types import EventType

from switch.utils.types import SCT, HandlerCallback
from switch.bots.handlers.event_handler import EventHandler
from switch.bots.bot_context import BotContext

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class CallbackQueryHandler(EventHandler):
    def __init__(
        self, callback: HandlerCallback[BotContext[CallbackQueryEvent], ResType], **kwargs
    ):
        super().__init__(EventType.CALLBACK_QUERY, callback, **kwargs)

    async def should_handle(self, context: BotContext[CallbackQueryEvent]) -> bool:
        return (
            await super().should_handle(context)
            and context.event.callback_query is not None
            and context.event.message is not None
        )
