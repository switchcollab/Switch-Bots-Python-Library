import re
from typing import TYPE_CHECKING, TypeVar
from switch.bots.constants import EventType, VALID_COMMAND_REGEX

from switch.utils.types import SCT, HandlerCallback
from switch.bots.handlers.base_handler import BaseHandler
from switch.bots.bot_context import BotContext
from switch.bots.events.command_event import CommandEvent

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class CommandHandler(BaseHandler):
    def __init__(
        self,
        command: SCT[str],
        callback: HandlerCallback[BotContext[CommandEvent], ResType],
        **kwargs,
    ):
        super().__init__(callback, **kwargs)
        if isinstance(command, str):
            commands = frozenset({command.lower()})
        else:
            commands = frozenset(x.lower() for x in command)
        for comm in commands:
            if not re.match(VALID_COMMAND_REGEX, comm):
                raise ValueError(f"Command `{comm}` is not a valid bot command.")
        self.commands = commands

    async def should_handle(self, context: BotContext[CommandEvent]) -> bool:
        if (
            context.event.type == EventType.COMMAND
            and context.event.message is not None
            and context.event.command in self.commands
            and context.event.message.user_id != context.bot.id
        ):
            return True
        return False
