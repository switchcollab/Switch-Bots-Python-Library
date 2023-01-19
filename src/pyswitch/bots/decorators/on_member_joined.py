from typing import Callable, Optional
import pyswitch
from pyswitch.bots.filters.filter import Filter


class OnMemberJoined:
    def on_member_joined(
        self: "pyswitch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling members joins."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyswitch.BotApp):
                self.add_handler(pyswitch.bots.handlers.MemberJoinedHandler(func, filter))

            return func

        return decorator
