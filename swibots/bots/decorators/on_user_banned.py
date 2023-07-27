from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter


class OnUserBanned:
    def on_user_banned(self: "swibots.BotApp" = None, filter: Optional[Filter] = None) -> Callable:
        """Decorator for handling user ban."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(swibots.bots.handlers.UserBannedHandler(func, filter))

            return func

        return decorator
