from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnGroupDeleted:
    def on_group_deleted(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling group deletions."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.GroupDeletedHandler(func, filter))

            return func

        return decorator
