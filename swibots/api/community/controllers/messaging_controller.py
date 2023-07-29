import logging
from typing import TYPE_CHECKING, List
from swibots.api.community.models import InstantMessaging

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/instant/messaging"


class InstantMessagingController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def enable_messages(
        self, community_id: str, group_id: str, bot_id: str | int = None
    ) -> InstantMessaging:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.get(
            f"{BASE_PATH}/enable",
            data={"communityId": community_id, "groupId": group_id, "botId": bot_id},
        )
        return self.client.build_object(InstantMessaging, response.data.get("result"))

    async def disable_messages(
        self, community_id: str, group_id: str, bot_id: str | int = None
    ) -> InstantMessaging:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.get(
            f"{BASE_PATH}/disable",
            data={"communityId": community_id, "groupId": group_id, "botId": bot_id},
        )
        return self.client.build_object(InstantMessaging, response.data.get("result"))

    async def get_messaging_enabled(self, community_id: str, group_id: str) -> List[InstantMessaging]:
        resp = await self.client.get(f"{BASE_PATH}/bots?communityId={community_id}&groupId={group_id}")
        return self.client.build_list(InstantMessaging, resp.data.get("result"))
