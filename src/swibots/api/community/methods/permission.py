import swibots

from swibots.api.community.models import RolePermission


class PermissionMethods:
    """
    Methods for managing permissions in a community.

    Args:
        client (swibots.ApiClient): The API client.
    """

    async def get_permission(
        self: "swibots.ApiClient", role_id: str
    ) -> RolePermission | None:
        """
        Get the permission with the specified role ID.

        Args:
            role_id: The ID of the permission.

        Returns:
            The permission with the specified role ID, or `None` if the permission does not exist.
        """

        return await self.community_service.permission.get_permission(role_id)

    async def add_permission(
        self: "swibots.ApiClient", permission: RolePermission
    ) -> bool:
        """
        Add a new permission.

        Args:
            permission: The permission to add.

        Returns:
            True if the permission was added successfully, False otherwise.
        """

        return await self.community_service.permission.add_permission(permission)

    async def update_permission(
        self: "swibots.ApiClient",
        permission: RolePermission,
        permission_id: int = 0,
        role_id: int = 0,
    ) -> bool:
        """
        Update an existing permission.

        Args:
            permission: The permission to update.
            permission_id: The ID of the permission to update.
            role_id: The role ID of the permission to update.

        Returns:
            True if the permission was updated successfully, False otherwise.
        """

        return await self.community_service.permission.update_permission(
            permission, permission_id, role_id
        )

    async def delete_permission(self: "swibots.ApiClient", permission_id: int) -> bool:
        """
        Delete a permission.

        Args:
            permission_id: The ID of the permission to delete.

        Returns:
            True if the permission was deleted successfully, False otherwise.
        """

        return await self.community_service.permission.delete_permission(permission_id)

    async def add_user_permission(
        self: "swibots.ApiClient",
        community_id: str,
        user_id: int,
        role_colour: str,
        role_name: str,
        permission: RolePermission,
    ) -> bool:
        """
        Add a permission to a user.

        Args:
            community_id: The ID of the community.
            user_id: The ID of the user.
            role_colour: The role color of the permission.
            role_name: The role name of the permission.
            permission: The permission to add.

        Returns:
            True if the permission was added successfully, False otherwise.
        """

        return await self.community_service.permission.add_user_permission(
            community_id, user_id, role_colour, role_name, permission
        )
