from typing import Type, TypeVar
import swibots
from swibots.api.common.models import User


class GetUser:
    async def get_user(self: "swibots.ApiClient", user_id: int) -> User:
        """Get User Info

        Args:
          user_id (`str` | `int`): The user id to fetch info.
        """
        return await self.chat_service.messages.get_user(user_id)

    async def get_last_seen(self: "swibots.ApiClient", user_id: int) -> int:
        """Get last seen of user

        Args:
            user_id (int): User ID

        Returns:
            int: timestamp when user was last active.
        """
        return await self.chat_service.posts.get_last_seen(user_id)
