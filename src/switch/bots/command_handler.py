import re
from typing import TYPE_CHECKING, TypeVar

from switch.utils.types import SCT, HandlerCallback
from switch.bots.base_handler import BaseHandler
from switch.bots.bot_context import BotContext
from switch.bots.request import Request

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")

class CommandHandler(BaseHandler):
    def __init__(self, command: SCT[str], callback: HandlerCallback[BotContext[Request],ResType], **kwargs):
        super().__init__(callback, **kwargs)
        if isinstance(command, str):
            commands = frozenset({command.lower()})
        else:
            commands = frozenset(x.lower() for x in command)
        for comm in commands:
            if not re.match(r"^[\da-z_]{1,32}$", comm):
                raise ValueError(f"Command `{comm}` is not a valid bot command.")
        self.commands = commands

    async def should_handle(self, context: BotContext[Request]) -> bool:
        if context.request.message is None:
            return False
        return True
    
