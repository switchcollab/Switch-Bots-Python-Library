from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter


class OnUnknownCommand:
    def on_unknown_command(
        self: "swibots.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling unknown commands."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(
                    swibots.bots.handlers.UnknownCommandHandler(func, filter)
                )

            return func

        return decorator
