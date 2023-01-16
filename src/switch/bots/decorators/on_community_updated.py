from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnCommunityUpdated:
    def on_community_update(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling new commands."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.CommunityUpdatedHandler(func, filter))

            return func

        return decorator
