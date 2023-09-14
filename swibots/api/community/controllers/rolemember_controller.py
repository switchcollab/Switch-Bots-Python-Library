import logging
from typing import TYPE_CHECKING, Optional, List

from swibots.api.common.models import User
from swibots.api.community.models import RoleMember


if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/member"


class RoleMemberController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def get_members(self, role_id: str) -> List[RoleMember]:
        """Get all members by role id"""
        response = await self.client.get(f"{BASE_PATH}/getAll?roleId={role_id}")
        return self.client.build_list(RoleMember, response.data.get("result"))

    async def add_member_to_role(
        self,
        community_id: str,
        member_id: int,
        role_ids: List[int],
    ) -> bool:
        data = {"communityId": community_id, "roleIds": role_ids, "memberId": member_id}
        response = await self.client.post(f"{BASE_PATH}/add", data=data)
        return response.data.get("success", False)

    async def delete_role_member(
        self,
        id: Optional[int] = None,
        member_id: Optional[int] = None,
        role_id: Optional[int] = None,
    ) -> bool:
        """delete member from role by id"""
        if id:
            response = await self.client.delete(f"{BASE_PATH}/delete/{id}")
        elif member_id and role_id:
            response = await self.client.delete(
                f"{BASE_PATH}/delete?memberId={member_id}&roleId={role_id}"
            )
        else:
            raise ValueError(
                "Either provide 'id' or 'member_id with role_id' to  delete member from the role."
            )
        return response.data.get("success", False)
