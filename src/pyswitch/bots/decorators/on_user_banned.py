from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnUserBanned:
    def on_user_banned(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling user ban."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.UserBannedHandler(func, filter))

            return func

        return decorator
