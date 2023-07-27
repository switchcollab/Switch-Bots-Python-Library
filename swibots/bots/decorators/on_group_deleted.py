from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter


class OnGroupDeleted:
    def on_group_deleted(
        self: "swibots.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling group deletions."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(swibots.bots.handlers.GroupDeletedHandler(func, filter))

            return func

        return decorator
