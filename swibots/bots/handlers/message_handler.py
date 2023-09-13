from typing import TYPE_CHECKING, Optional, TypeVar
from swibots.api.chat.events import MessageEvent
from swibots.bots.filters.filter import Filter

from swibots.bots.handlers import BaseHandler
from swibots.bots import BotContext
from .event_handler import EventHandler
from swibots.types import EventType
from swibots.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class MessageHandler(EventHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[MessageEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.MESSAGE, callback, filter, **kwargs)

    async def should_handle(self, context: BotContext[MessageEvent]) -> bool:
        return (
            await super().should_handle(context)
            and context.event.message is not None
            and context.event.message.user_id != context.app.user.id
        )
