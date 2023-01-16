from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnGroupUpdated:
    def on_group_updated(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling group updates."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.GroupUpdatedHandler(func, filter))

            return func

        return decorator
