import logging
from typing import TYPE_CHECKING, List
from datetime import timedelta, datetime
from swibots.api.community.models import RestrictedUser

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/restrict"


class RestrictController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def list_restricted_users(self, community_id: str) -> List[RestrictedUser]:
        response = await self.client.get(
            f"{BASE_PATH}/users?communityId={community_id}"
        )
        return self.client.build_list(RestrictedUser, response.data)

    async def get_restricted_user(self, community_id: str, user_id: int):
        response = await self.client.get(
            f"{BASE_PATH}/user?communityId={community_id}&userId={user_id}"
        )
        return self.client.build_object(RestrictedUser, response.data.get("result"))

    async def restrict_user(
        self,
        community_id: str,
        restricted: bool,
        user_id: int,
        until_date: int = 0,
    ) -> bool:
        await self.client.post(
            f"{BASE_PATH}/user",
            data={
                "communityId": community_id,
                "restricted": restricted,
                "restrictedTillTimestamp": until_date,
                "userId": user_id,
            },
        )
        return True

    async def update_restricted_user(
        self,
        community_id: str,
        restricted: bool,
        user_id: int,
        until_date: int = 0,
    ) -> bool:
        await self.client.put(
            f"{BASE_PATH}/user",
            data={
                "communityId": community_id,
                "restricted": restricted,
                "restrictedTillTimestamp": until_date,
                "userId": user_id,
            },
        )
        return True
