from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnChannelDeleted:
    def on_channel_created(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling channel creations."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.ChannelDeletedHandler(func, filter))

            return func

        return decorator
