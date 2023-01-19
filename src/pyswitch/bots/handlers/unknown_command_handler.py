import re
from typing import TYPE_CHECKING, Any, Optional, TypeVar
from pyswitch.bots.constants import VALID_COMMAND_REGEX
from pyswitch.bots.filters.filter import Filter
from pyswitch.types import EventType

from pyswitch.utils.types import SCT, HandlerCallback
from pyswitch.bots.handlers.base_handler import BaseHandler
from pyswitch.bots.bot_context import BotContext

if TYPE_CHECKING:
    pass

ResType = TypeVar("ResType")


class UnknownCommandHandler(BaseHandler):
    def __init__(
        self,
        callback: HandlerCallback[BotContext[Any], ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        super().__init__(callback, filter, **kwargs)

    async def should_handle(self, context: BotContext[Any]) -> bool:
        if context.event.type == EventType.COMMAND and context.event.message is not None:
            return True
        return False
