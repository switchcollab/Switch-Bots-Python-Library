from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter
from switch.utils.types import SCT


class OnCommand:
    def on_command(
        self: "switch.BotApp", command: SCT[str], filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling new commands."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.CommandHandler(command, func, filter))

            return func

        return decorator
