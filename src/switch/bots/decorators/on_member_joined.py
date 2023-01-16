from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnMemberJoined:
    def on_member_joined(
        self: "switch.BotApp" = None, filter: Optional[Filter] = None
    ) -> Callable:
        """Decorator for handling members joins."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.MemberJoinedHandler(func, filter))

            return func

        return decorator
