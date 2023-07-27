import swibots
from typing import List, Optional

from swibots.api.common.models import User
from swibots.api.community.models import RoleMember


class RoleMemberMethods:
    """
    Methods for managing member linked with role in a community.

    Args:
        client (swibots.ApiClient): The API client.
    """


    async def get_members(self: "swibots.ApiClient", role_id: str) -> List[RoleMember]:
        """
        Get the members of the role with the specified role ID.

        Args:
            role_id: The ID of the role.

        Returns:
            A list of the members of the role.
        """

        return await self.community_service.rolemember.get_members(role_id)


    async def add_member_to_role(
            self: "swibots.ApiClient",
            community_id: str,
            member_id: int,
            role_id: int,
            user_id: int,
            user: User,
            id: Optional[int] = None,
        ) -> bool:
        """
        Add a member to the role with the specified role ID.

        Args:
            community_id: The ID of the community.
            member_id: The ID of the member.
            role_id: The ID of the role.
            user_id: The ID of the user who is adding the member to the role.
            user: The user who is adding the member to the role.
            id: The ID of the role member, if it already exists.

        Returns:
            True if the member was added successfully, False otherwise.
        """

        return await self.community_service.rolemember.add_member_to_role(community_id, member_id, role_id, user_id, user, id)


    async def delete_role_member(
            self: "swibots.ApiClient",
            id: Optional[int] = None,
            member_id: Optional[int] = None,
            role_id: Optional[int] = None,
        ) -> bool:
        """
        Delete the role member with the specified ID.

        Args:
            id: The ID of the role member.
            member_id: The ID of the member.
            role_id: The ID of the role.

        Returns:
            True if the role member was deleted successfully, False otherwise.
        """

        return await self.community_service.rolemember.delete_role_member(id, member_id, role_id)