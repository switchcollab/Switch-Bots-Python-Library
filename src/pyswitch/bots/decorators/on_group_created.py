from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnGroupCreated:
    def on_group_created(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling group creations."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.GroupCreatedHandler(func, filter))

            return func

        return decorator
