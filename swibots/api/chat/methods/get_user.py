from typing import Type, TypeVar
import swibots
from swibots.api.common.models import User
from swibots.api.chat.models import SessionInfo


class GetUser:
    async def get_user(
        self: "swibots.ApiClient", user_id: int = None, username: str = None
    ) -> User:
        """Get User Info from user_id or username

        Args:
          user_id Optional(`int`): The user id to fetch info.
          username [Optional(`str`)]: The username.

        Raises:
          ValueError: if both user_id and username are provided or both are missing!

        """
        return await self.chat_service.messages.get_user(user_id, username=username)

    async def get_session_info(
        self: "swibots.ApiClient", session_id: str
    ) -> SessionInfo:
        """Get session info from session id

        Args:
            session_id (str): session id to get info.

        Returns:
            SessionInfo:
        """
        return await self.chat_service.posts.get_session_info(session_id=session_id)

    async def get_last_seen(self: "swibots.ApiClient", user_id: int) -> int:
        """Get last seen of user

        Args:
            user_id (int): User ID

        Returns:
            int: timestamp when user was last active.
        """
        return await self.chat_service.posts.get_last_seen(user_id)
