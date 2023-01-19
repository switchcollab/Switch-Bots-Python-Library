from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnMessage:
    def on_message(self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None) -> Callable:
        """Decorator for handling new messages."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.MessageHandler(func, filter))

            return func

        return decorator
