import logging
from typing import TYPE_CHECKING

from swibots.api.community.models import Role, RolePermission


if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/roles"


class RolesController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def get_roles(self, community_id: str):
        """Get all roles by community id"""
        response = await self.client.get(
            f"{BASE_PATH}/getAll?communityId={community_id}"
        )
        return self.client.build_list(Role, response.data.get("result"))

    async def add_role(
        self, community_id: str, role_colour: str, role_name: str
    ) -> Role:
        """Add role to the community"""
        role = Role(
            app=self.client.app,
            community_id=community_id,
            colour=role_colour,
            name=role_name,
        )
        await self.client.post(
            f"{BASE_PATH}/add?communityId={community_id}",
            data=role.to_json_request(),
        )
        return role

    async def update_role(
        self,
        community_id: str,
        role_id: int,
        role_colour: str = None,
        role_name: str = None,
    ) -> bool:
        """update role by community and role id"""
        await self.client.put(
            f"{BASE_PATH}/update",
            data=Role(
                app=self.client.app,
                colour=role_colour,
                community_id=community_id,
                name=role_name,
                id=role_id,
            ).to_json_request(),
        )
        return True

    async def delete_role(self, roleId: int):
        """delete role by id"""
        response = await self.client.delete(f"{BASE_PATH}/delete/{roleId}")
        return response.data.get("success")
