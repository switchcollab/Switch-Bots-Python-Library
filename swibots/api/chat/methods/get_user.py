from typing import Type, TypeVar
import swibots
from swibots.api.common.models import User


class GetUser:
    async def get_user(self: "swibots.ApiClient", user_id: int | str) -> User:
        """Get User Info

        Args:
          user_id (`str` | `int`): The user id to fetch info.
        """
        return await self.chat_service.messages.get_user(user_id)