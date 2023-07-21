from typing import List, Optional
import swibots
from swibots.api.airdrop.models import Referral


class GetReferrals:
    async def get_referral(
        self: "swibots.ApiClient", tournament_id: str | int
    ) -> List[Referral]:
        """Get referrals from tournament_id

        Args:
            tournament_id: The Tournament ID to get referrals for.

        Returns:
            A list of referrals.
        """
        return await self.airdrop_service.tournament.get_referrals(tournament_id)
