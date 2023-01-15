import re
from typing import TYPE_CHECKING, Any, TypeVar
from switch.bots.constants import VALID_COMMAND_REGEX
from switch.types import EventType

from switch.utils.types import SCT, HandlerCallback
from switch.bots.handlers.base_handler import BaseHandler
from switch.bots.bot_context import BotContext

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class UnknownCommandHandler(BaseHandler):
    def __init__(self, callback: HandlerCallback[BotContext[Any], ResType], **kwargs):
        super().__init__(callback, **kwargs)

    async def should_handle(self, context: BotContext[Any]) -> bool:
        if context.event.type == EventType.COMMAND and context.event.message is not None:
            return True
        return False
