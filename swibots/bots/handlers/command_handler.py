import re
from typing import TYPE_CHECKING, Optional, TypeVar
from swibots.bots.constants import VALID_COMMAND_REGEX
from swibots.bots.filters.filter import Filter
from swibots.types import EventType

from swibots.utils.types import SCT, HandlerCallback
from swibots.bots.handlers.event_handler import EventHandler
from swibots.bots.bot_context import BotContext
from swibots.api.chat.events import CommandEvent

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class CommandHandler(EventHandler):
    def __init__(
        self,
        command: SCT[str],
        callback: HandlerCallback[BotContext[CommandEvent], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(EventType.COMMAND, callback, filter, **kwargs)
        if isinstance(command, str):
            commands = frozenset({command.lower()})
        else:
            commands = frozenset(x.lower() for x in command)
        for comm in commands:
            if not re.match(VALID_COMMAND_REGEX, comm):
                raise ValueError(f"Command `{comm}` is not a valid bot command.")
        self.commands = commands

    async def should_handle(self, context: BotContext[CommandEvent]) -> bool:
        return (
            await super().should_handle(context)
            and context.event.command is not None
            and context.event.command in self.commands
            and context.event.message.user_id != context.bot.id
            and context.event.message is not None
        )
