import logging
from typing import TYPE_CHECKING

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
        return response.data.get("channelId")

    async def update_channel(self, channel: Channel) -> str:
        response = await self.client.put(BASE_PATH, data=channel.to_json_request())
        return response.data.get("channelId")