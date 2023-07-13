import swibots

from swibots.api.community.models import Channel


class UnbanUser:
    async def unban_user(
        self: "swibots.ApiClient", unban: bool, community_id: str, id: int, user_id: str
    ):
        """Unbans a user in a community.

        Args:
            unban (bool): Whether the user should be unbanned.
            community_id (str): The ID of the community.
            id (int): The ID of the user to unban.
            user_id (str): The ID of the user to unban.

        Returns:
            bool: Whether the unban was successful.
        """
        return await self.community_service.ban.unban_user(
            unban, community_id, id, user_id
        )
