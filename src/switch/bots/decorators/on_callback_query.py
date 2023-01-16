from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnCallbackQuery:
    def on_callback_query(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling callback queries."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.CallbackQueryHandler(func, filter))

            return func

        return decorator
