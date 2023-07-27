import logging
from typing import TYPE_CHECKING

from swibots.api.community.models import Role, RolePermission


if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/permission"


class PermissionController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def get_permission(self, role_id: str) -> RolePermission | None:
        """Get permission by role id"""
        response = await self.client.get(f"{BASE_PATH}/get/?roleId={role_id}")
        return self.client.build_object(RolePermission, response.data.get("result"))

    async def add_permission(self, permission: RolePermission) -> bool:
        """Add permission"""
        response = await self.client.post(
            f"{BASE_PATH}/add", data=permission.to_json_request()
        )
        return response.data.get("success", False)

    async def update_permission(
        self,
        permission: RolePermission = None,
        permission_id: int = 0,
        role_id: int = 0,
    ) -> bool:
        """update permission"""
        if id:
            permission.id = permission_id
        if role_id:
            permission.role_id = role_id

        await self.client.put(
            f"{BASE_PATH}/update",
            data=permission.to_json_request(),
        )
        return True

    async def delete_permission(self, permission_id: int) -> bool:
        """delete permission by id"""
        response = await self.client.delete(f"{BASE_PATH}/delete/{permission_id}")
        return response.data.get("success", False)

    async def add_user_permission(
        self,
        community_id: str,
        user_id: int,
        role_colour: str,
        role_name: str,
        permission: RolePermission,
    ) -> bool:
        resp = await self.client.post(
            f"{BASE_PATH}/user",
            data={
                "communityId": community_id,
                "memberId": user_id,
                "roleColour": role_colour,
                "roleName": role_name,
                "rolePermission": permission.to_json()["rolePermission"],
            },
        )
        return resp.data.get("success", False)
