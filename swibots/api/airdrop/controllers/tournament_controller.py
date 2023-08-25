import json
import logging
from typing import TYPE_CHECKING, List
from swibots.api.airdrop.models import Referral, Tournament
from swibots.errors import SwitchError
from swibots.utils.types import JSONDict

if TYPE_CHECKING:
    from swibots.api.airdrop import AirdropClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/tournament"


class TournamentController:
    """Airdrop controller

    This controller is used to communicate with the airdrop endpoints.
    """

    def __init__(self, client: "AirdropClient"):
        self.client = client

    async def get_referrals(self, id: str | int, user_id: str | int) -> List[Referral]:
        """Get referrals"""
        response = await self.client.get(
            f"{BASE_PATH}/getUserReferrals/{id}?user_id={user_id}"
        )
        return self.client.build_list(Referral, response.data)

    async def get_tournaments(self, community_id: str) -> List[Tournament]:
        """Get tournaments by community_id"""
        response = await self.client.get(
            f"{BASE_PATH}/getTournamentsByCommunityId/{community_id}"
        )
        return self.client.build_list(Tournament, response.data)
