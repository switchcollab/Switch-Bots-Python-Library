from typing import List, Optional
import swibots
from swibots.api.airdrop.models import Tournament


class GetTournaments:
    async def get_tournaments(
        self: "swibots.ApiClient", community_id: str
    ) -> List[Tournament]:
        """Get tournaments from community_id

        Args:
            community_id: community id to get tournaments from.

        Returns:
            A list of tournaments
        """
        return await self.airdrop_service.tournament.get_tournaments(community_id)
