from typing import Callable
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnChannelCreated:
    def on_channel_created(self: "pyswitch.BotApp" = None, filter: Filter = None) -> Callable:
        """Decorator for handling channel creations."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.ChannelCreatedHandler(func, filter))

            return func

        return decorator
