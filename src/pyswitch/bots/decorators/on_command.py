from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter
from pyswitch.utils.types import SCT


class OnCommand:
    def on_command(
        self: "pyswitch.BotApp", command: SCT[str], filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling new commands."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.CommandHandler(command, func, filter))

            return func

        return decorator
