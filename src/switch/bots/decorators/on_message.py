from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnMessage:
    def on_message(self: "switch.BotApp" = None, filter: Optional[Filter] = None) -> Callable:
        """Decorator for handling new messages."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.MessageHandler(func, filter))

            return func

        return decorator
