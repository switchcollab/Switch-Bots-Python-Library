from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnGroupCreated:
    def on_group_created(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling group creations."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.GroupCreatedHandler(func, filter))

            return func

        return decorator
