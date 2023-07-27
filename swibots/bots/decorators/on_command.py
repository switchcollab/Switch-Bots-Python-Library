from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter
from swibots.utils.types import SCT


class OnCommand:
    def on_command(
        self: "swibots.BotApp", command: SCT[str], filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling new commands."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(swibots.bots.handlers.CommandHandler(command, func, filter))

            return func

        return decorator
