import logging
from typing import TYPE_CHECKING, List
from swibots.api.community.models import Group
from swibots.errors import SwitchError

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/group"


class GroupController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def get_group(self, group_id: str):
        """Get a channel by id"""
        response = await self.client.get(f"{BASE_PATH}?groupId={group_id}")
        return self.client.build_object(Group, response.data.get("result"))

    async def get_all_groups(self, community_id: str) -> List[Group]:
        response = await self.client.get(f"{BASE_PATH}/all?communityId={community_id}")
        return self.client.build_list(Group, response.data.get("result"))

    async def create_group(self, group: Group) -> str:
        response = await self.client.post(BASE_PATH, data=group.to_json_request())
        return response.data.get("result", {}).get("groupId")

    async def delete_group(self, group_id: str) -> bool:
        response = await self.client.delete(f"{BASE_PATH}/{group_id}")
        if response.status_code == 200:
            return True
        logging.debug(response.data)
        if err:= response.data.get("errorMessage"):
            raise SwitchError(err)
        return False

    async def update_group(self, group: Group) -> str:
        response = await self.client.put(BASE_PATH, data=group.to_json_request())
        return response.data.get("result", {}).get("groupId")
