import swibots


class BanUser:
    async def ban_user(self: "swibots.ApiClient", community_id: str, user_id: str):
        """
        Bans a user in a community.

        Args:
            community_id (str): The ID of the community.
            user_id (str): The ID of the user to ban.

        Returns:
            bool: Whether the ban was successful.
        """
        return await self.community_service.ban.ban_user(community_id, user_id)
