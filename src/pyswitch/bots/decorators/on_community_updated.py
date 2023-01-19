from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnCommunityUpdated:
    def on_community_update(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling new commands."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.CommunityUpdatedHandler(func, filter))

            return func

        return decorator
