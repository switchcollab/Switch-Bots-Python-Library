import logging
from typing import TYPE_CHECKING
from swibots.api.community.models import Channel, Community, Group

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community"


class CommunityController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def get_community(self, community_id: str):
        """Get a community by id"""
        response = await self.client.get(f"{BASE_PATH}?communityId={community_id}")
        return self.client.build_object(Community, response["result"])
