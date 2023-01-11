import re
from typing import TYPE_CHECKING, TypeVar
from switch.bots.command_event import CommandEvent
from switch.bots.constants import EventType, VALID_COMMAND_REGEX

from switch.utils.types import SCT, HandlerCallback
from switch.bots.base_handler import BaseHandler
from switch.bots.bot_context import BotContext
from switch.bots.event import Event

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class UnknownCommandHandler(BaseHandler):
    def __init__(self, callback: HandlerCallback[BotContext[CommandEvent], ResType], **kwargs):
        super().__init__(callback, **kwargs)

    async def should_handle(self, context: BotContext[CommandEvent]) -> bool:
        if context.event.type == EventType.COMMAND and context.event.message is not None:
            return True
        return False
