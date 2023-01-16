from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnGroupDeleted:
    def on_group_deleted(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling group deletions."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.GroupDeletedHandler(func, filter))

            return func

        return decorator
