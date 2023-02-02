from typing import Callable, Optional
import swibots
from swibots.bots.filters.filter import Filter


class OnInlineQuery:
    def on_inline_query(self: "swibots.BotApp" = None, filter: Optional[Filter] = None) -> Callable:
        """Decorator for handling new messages."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, swibots.BotApp):
                self.add_handler(
                    swibots.bots.handlers.InlineQueryHandler(func, filter))

            return func

        return decorator
