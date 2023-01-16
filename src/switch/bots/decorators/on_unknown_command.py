from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnUnknownCommand:
    def on_unknown_command(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling unknown commands."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.UnknownCommandHandler(func, filter))

            return func

        return decorator
