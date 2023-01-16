from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnChannelUpdated:
    def on_channel_updated(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling channel update."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.ChannelUpdatedHandler(func, filter))

            return func

        return decorator
