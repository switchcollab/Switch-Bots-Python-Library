import swibots
from typing import Optional
from swibots.api.community.models import Channel


class DeductXP:
    async def deduct_xp(
        self: "swibots.ApiClient",
        community_id: str,
        user_id: str,
        xp: int = 0,
        description: Optional[str] = None,
    ) -> bool:
        """
        Deducts XP from a user in a community.

        Args:
            community_id: The ID of the community.
            user_id: The ID of the user.
            xp: The amount of XP to deduct.
            description: An optional description of the reason for the deduction.

        Returns:
            True if the deduction was successful, False otherwise.
        """
        return await self.community_service.communities.deduct_xp(
            community_id, user_id, xp, description
        )
