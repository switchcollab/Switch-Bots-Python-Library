from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter


class OnCallbackQuery:
    def on_callback_query(
        self: "swibots.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling callback queries."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(
                    swibots.bots.handlers.CallbackQueryHandler(func, filter)
                )

            return func

        return decorator
