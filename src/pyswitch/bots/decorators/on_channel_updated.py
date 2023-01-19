from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnChannelUpdated:
    def on_channel_updated(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling channel update."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.ChannelUpdatedHandler(func, filter))

            return func

        return decorator
