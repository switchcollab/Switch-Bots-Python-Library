from typing import List, Optional
import swibots
from swibots.api.airdrop.models import Referral


class GetReferrals:
    async def get_referral(
        self: "swibots.ApiClient", id: str | int
    ) -> List[Referral]:
        """Get referrals from user_id

        Args:
            id: The user ID to get referrals for.

        Returns:
            A list of referrals.
        """
        return await self.airdrop_service.tournament.get_referrals(id)
