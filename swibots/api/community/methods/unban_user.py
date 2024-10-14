import swibots

from swibots.api.community.models import Channel


class UnbanUser:
    async def unban_user(
        self: "swibots.ApiClient",  community_id: str, user_id: str
    ):
        """Unbans a user in a community.

        Args:
            community_id (str): The ID of the community.
            user_id (str): The ID of the user to unban.

        Returns:
            bool: Whether the unban was successful.
        """
        return await self.community_service.ban.unban_user(community_id, user_id)
