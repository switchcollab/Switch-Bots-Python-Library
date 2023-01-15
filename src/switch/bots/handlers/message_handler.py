from typing import TYPE_CHECKING, TypeVar
from switch.api.chat.events import MessageEvent

from switch.bots.handlers import BaseHandler
from switch.bots import BotContext
from .event_handler import EventHandler
from switch.types import EventType
from switch.utils.types import HandlerCallback

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class MessageHandler(EventHandler):
    def __init__(self, callback: HandlerCallback[BotContext[MessageEvent], ResType], **kwargs):
        super().__init__(EventType.MESSAGE, callback, **kwargs)

    async def should_handle(self, context: BotContext[MessageEvent]) -> bool:
        return (
            await super().should_handle(context)
            and context.event.message is not None
            and context.event.message.user_id != context.bot.id
        )
