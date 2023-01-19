from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnGroupUpdated:
    def on_group_updated(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling group updates."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.GroupUpdatedHandler(func, filter))

            return func

        return decorator
