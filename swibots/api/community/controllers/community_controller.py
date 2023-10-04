import logging
from typing import TYPE_CHECKING, Optional, List
from ..models import InstantMessaging
from swibots.api.community.models import Community, CommunityMember
from swibots.api.bot.models import BotInfo
from swibots.api.common.models import User
from urllib.parse import urlencode

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community"


class CommunityController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def get_community(self, community_id: str = "", username: str = ""):
        """Get a community by id or username"""
        if not (community_id or username):
            raise ValueError("community_id or username must be provided.")

        if community_id and username:
            raise ValueError("community_id and username can't be provided together.")
        if username:
            request_url = f"{BASE_PATH}/communityusername?communityUsername={username}"
        else:
            request_url = f"{BASE_PATH}?communityId={community_id}"
        response = await self.client.get(request_url)
        return self.client.build_object(Community, response.data.get("result"))

    async def deduct_xp(
        self,
        community_id: str,
        user_id: str,
        xp: int = 0,
        description: Optional[str] = None,
    ) -> bool:
        response = await self.client.get(
            f"{BASE_PATH}/deductXP",
            data={
                "communityId": community_id,
                "description": description,
                "userId": user_id,
                "xp": xp,
            },
        )
        return response.data.get("success", False)

    async def get_community_member(
        self, community_id: str, user_id: int
    ) -> CommunityMember:
        response = await self.client.get(
            f"{BASE_PATH}/user?communityId={community_id}&userId={user_id}"
        )
        return self.client.build_object(CommunityMember, response.data.get("result"))

    async def get_community_members(self, community_id: str) -> List[CommunityMember]:
        response = await self.client.get(
            f"{BASE_PATH}/users?communityId={community_id}"
        )
        members = self.client.build_list(
            CommunityMember, response.data.get("result", {}).get("communityMembers")
        )
        userInfo = {
            int(x["id"]): x for x in response.data.get("result", {}).get("userInfoList")
        }
        for community_member in members:
            if data := userInfo.get(community_member.user_id):
                community_member.user = self.client.build_object(User, data)

        return members

    # region

    async def approve_chat_join(
        self,
        members: Optional[int] = None,
        channel_id: Optional[str] = None,
        community_id: Optional[str] = None,
        group_id: Optional[str] = None,
        decline: Optional[bool] = None,
    ):
        await self.client.get(
            f"{BASE_PATH}/members/private/accept",
            data={
                "channelId": channel_id,
                "communityId": community_id,
                "decline": decline,
                "groupId": group_id,
                "members": members,
            },
        )

    # endregion

    # region
    # Commands

    async def get_active_commands(
        self, community_id: str, channel_id: str = None, group_id: Optional[str] = None
    ) -> List[BotInfo]:
        data = {
            "channelId": channel_id or group_id,
            "isGroup": bool(group_id),
            "communityId": community_id,
        }
        response = await self.client.get(
            f"{BASE_PATH}/activecommands?{urlencode(data)}"
        )
        response_data = response.data.get("result", {}).get("channelOrGroup", {})
        return self.client.build_list(BotInfo, response_data.get("bots"))

    # endregion

    # region

    async def is_community_member(self, community_id: str, user_id: int) -> bool:
        response = await self.client.get(
            f"{BASE_PATH}/validate/user/member?communityId={community_id}&user_id={user_id}"
        )
        return response.data.get("result", {}).get("member")

    # endregion

    # region
    async def get_messaging_bots(
        self,
        community_id: str,
        channel_id: Optional[str] = None,
        group_id: Optional[str] = None,
        bot_id: Optional[str] = None,
    ) -> List[InstantMessaging]:
        data = {
            "botId": bot_id,
            "communityId": community_id,
            "channelId": channel_id,
            "groupId": group_id,
        }
        response = await self.client.get(
            f"{BASE_PATH}/instant/messaging/bots?{urlencode(data)}"
        )
        return self.client.build_list(InstantMessaging, response.data.get("result"))

    # endregion
