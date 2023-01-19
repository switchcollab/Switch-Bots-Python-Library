from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnChannelDeleted:
    def on_channel_created(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling channel creations."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.ChannelDeletedHandler(func, filter))

            return func

        return decorator
