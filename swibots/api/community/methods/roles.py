import swibots

from swibots.api.community.models import Role
from typing import List


class RoleMethods:
    """
    Methods for managing roles in a community.

    Args:
        client (swibots.ApiClient): The API client.
    """

    async def add_role(
        self: "swibots.ApiClient",
        community_id: str,
        name: str,
        colour: str,
    ) -> Role:
        """
        Add a new role to a community.

        Args:
            community_id (str): The ID of the community.
            name (str): The name of the role.
            colour (str): The color of the role.

        Returns:
            :obj:`swibots.api.community.models.Role`: The new role.
        """

        return await self.community_service.roles.add_role(
            community_id=community_id, role_colour=colour, role_name=name
        )

    async def get_roles(self: "swibots.ApiClient", community_id: str) -> List[Role]:
        """
        Retrieve all roles in a community.

        Args:
            community_id (str): The ID of the community.

        Returns:
            List[:obj:`swibots.api.community.models.Role`]: A list of all roles in the community.
        """

        return await self.community_service.roles.get_roles(community_id)

    async def delete_role(self: "swibots.ApiClient", role_id: str):
        """
        Delete a role from a community.

        Args:
            role_id (str): The ID of the role to delete.
        """

        return await self.community_service.roles.delete_role(role_id)

    async def update_role(
        self: "swibots.ApiClient",
        community_id: str,
        role_id: int,
        role_colour: str,
        role_name: str,
    ):
        """
        Update a role in a community.

        Args:
            community_id (str): The ID of the community.
            role_id (int): The ID of the role to update.
            role_colour (str): The new color of the role.
            role_name (str): The new name of the role.

        Returns:
            :obj:`swibots.api.community.models.Role`: The updated role.
        """

        return await self.community_service.roles.update_role(
            community_id, role_id, role_colour, role_name
        )
