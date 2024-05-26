import logging
from typing import TYPE_CHECKING, List

from swibots.api.community.models import Channel


if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/channel"


class ChannelController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def get_channel(self, channel_id: str):
        """Get a channel by id"""
        response = await self.client.get(f"{BASE_PATH}?channelId={channel_id}")
        return self.client.build_object(Channel, response.data.get("result"))

    async def create_channel(self, channel: Channel) -> str:
        response = await self.client.post(BASE_PATH, data=channel.to_json_request())
        return response.data.get("result", {}).get("channelId")

    async def delete_channel(self, channel_id: str) -> str:
        response = await self.client.delete(f"{BASE_PATH}/{channel_id}")
        # return response.data.get("result", {}).get("channelId")
        return (
            "Successfully deleted the channel."
            if response.status_code == 200
            else response.data.get("errorMessage")
        )

    async def update_channel(self, channel: Channel) -> str:
        response = await self.client.put(BASE_PATH, data=channel.to_json_request())
        return response.data.get("result", {}).get("channelId")

    async def get_all_channels(self, community_id: str) -> List[Channel]:
        response = await self.client.get(f"{BASE_PATH}/all?communityId={community_id}")
        return self.client.build_list(Channel, response.data.get("result"))
