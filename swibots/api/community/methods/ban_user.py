import swibots
from swibots.api.community.models import BanInfo


class BanUser:
    async def ban_user(
        self: "swibots.ApiClient", community_id: str, user_id: str
    ) -> BanInfo:
        """
        Bans a user in a community.

        Args:
            community_id (str): The ID of the community.
            user_id (str): The ID of the user to ban.
        """
        return await self.community_service.ban.ban_user(community_id, user_id)
