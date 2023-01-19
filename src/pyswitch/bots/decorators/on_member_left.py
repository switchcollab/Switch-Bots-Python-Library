from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnMemberLeft:
    def on_member_leaft(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling members joins."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.MemberLeftHandler(func, filter))

            return func

        return decorator
