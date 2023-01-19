from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter


class OnChannelUpdated:
    def on_channel_updated(
        self: "swibots.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling channel update."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(swibots.bots.handlers.ChannelUpdatedHandler(func, filter))

            return func

        return decorator
