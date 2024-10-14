import logging
from typing import TYPE_CHECKING
from swibots.api.community.models import BanInfo

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/ban"


class BanController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def ban_user(self, community_id: str, user_id: str):
        """ban a user from community"""
        response = await self.client.post(
            f"{BASE_PATH}", data={"communityId": community_id, "userId": user_id}
        )
        return self.client.build_object(BanInfo, response.data.get("result"))

    async def unban_user(self,  community_id: str,  user_id: str):
        response = await self.client.post(
            f"{BASE_PATH}/unban",
            data={
                "communityId": community_id,
                "userId": user_id,
            },
        )
        return response.data.get("result")
