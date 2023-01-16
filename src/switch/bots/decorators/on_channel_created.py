from typing import Callable
import switch
from switch.bots.filters.filter import Filter


class OnChannelCreated:
    def on_channel_created(self: "switch.BotApp" = None, filter: Filter = None) -> Callable:
        """Decorator for handling channel creations."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.ChannelCreatedHandler(func, filter))

            return func

        return decorator
