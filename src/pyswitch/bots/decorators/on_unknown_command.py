from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnUnknownCommand:
    def on_unknown_command(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling unknown commands."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.UnknownCommandHandler(func, filter))

            return func

        return decorator
