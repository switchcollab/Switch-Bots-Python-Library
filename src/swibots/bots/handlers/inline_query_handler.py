from typing import TYPE_CHECKING, Optional, TypeVar
from swibots.api.chat.events import InlineQueryEvent
from swibots.bots.filters.filter import Filter

from swibots.bots.handlers import BaseHandler
from swibots.bots import BotContext
from .event_handler import EventHandler
from swibots.types import EventType
from swibots.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class InlineQueryHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[InlineQueryEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.INLINE_QUERY, callback, filter, **kwargs)

    async def should_handle(self, context: BotContext[InlineQueryEvent]) -> bool:
        return (
            await super().should_handle(context)
        )
