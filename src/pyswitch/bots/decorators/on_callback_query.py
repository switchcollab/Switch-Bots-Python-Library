from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnCallbackQuery:
    def on_callback_query(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling callback queries."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.CallbackQueryHandler(func, filter))

            return func

        return decorator
