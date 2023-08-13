import logging
from typing import TYPE_CHECKING, List, Optional
from swibots.api.community.models import InstantMessaging

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/instant/messaging"


class InstantMessagingController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def enable_messages(
        self, community_id: str, channel_id: Optional[str] = None,  group_id: Optional[str] = None, bot_id: str | int = None
    ) -> InstantMessaging:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.post(
            f"{BASE_PATH}/enable",
            data={"communityId": community_id, "groupId": group_id, "botId": bot_id, "channelId": channel_id},
        )
        return self.client.build_object(InstantMessaging, response.data.get("result"))

    async def disable_messages(
        self, community_id: str, channel_id: Optional[str] = None, group_id: Optional[str] = None, bot_id: str | int = None
    ) -> InstantMessaging:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.post(
            f"{BASE_PATH}/disable",
            data={"communityId": community_id, "groupId": group_id, "botId": bot_id, "channelId": channel_id},
        )
        return self.client.build_object(InstantMessaging, response.data.get("result"))

    async def get_messaging_enabled(self, community_id: str, channel_id: Optional[str] = None, group_id: Optional[str] = None) -> List[InstantMessaging]:
        uri = f"{BASE_PATH}/bots?communityId={community_id}"
        if group_id:
           uri += f"&groupId={group_id}"
        else:
           uri += f"&channelId={channel_id}"
        resp = await self.client.get(uri)
        return self.client.build_list(InstantMessaging, resp.data.get("result"))
