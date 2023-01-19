import re
from typing import TYPE_CHECKING, Optional, TypeVar
from swibots.api.chat.events import CallbackQueryEvent
from swibots.bots.filters.filter import Filter
from swibots.types import EventType

from swibots.utils.types import SCT, HandlerCallback
from swibots.bots.handlers.event_handler import EventHandler
from swibots.bots.bot_context import BotContext

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class CallbackQueryHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[CallbackQueryEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.CALLBACK_QUERY, callback, filter, **kwargs)

    async def should_handle(self, context: BotContext[CallbackQueryEvent]) -> bool:
        return (
            await super().should_handle(context)
            and context.event.callback_data is not None
            and context.event.message is not None
        )
