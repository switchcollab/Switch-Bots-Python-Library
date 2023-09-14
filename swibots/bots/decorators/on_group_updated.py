from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter


class OnGroupUpdated:
    def on_group_updated(
        self: "swibots.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling group updates."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(
                    swibots.bots.handlers.GroupUpdatedHandler(func, filter)
                )

            return func

        return decorator
