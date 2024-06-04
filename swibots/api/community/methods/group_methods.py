import swibots

from typing import List
from swibots.api.community.models import Group


class GroupMethods:
    async def get_group(self: "swibots.ApiClient", id: str) -> Group:
        """Get a community by its ID

        Args:
            id (`str`): The ID of the group

        Returns:
            :obj:`swibots.api.community.models.Group`: The group object.

        Raises:
            :obj:`switch.error.SwitchError`: If the group could not be retrieved

        This method does the same as :meth:`switch.api.community.controllers.GroupController.get_group`.
        """
        return await self.community_service.groups.get_group(id)

    async def get_all_groups(
        self: "swibots.ApiClient", community_id: str
    ) -> List[Group]:
        """
        Get all groups from the community.
        """
        return await self.community_service.groups.get_all_groups(community_id)

    async def create_group(self: "swibots.ApiClient", group: Group) -> str:
        """Create group

        Args:
            :obj:`swibots.api.community.models.Group`: The group object.

        Returns:
            str:  group id

        Raises:
            :obj:`switch.error.SwitchError`: If the group could not be retrieved

        This method does the same as :meth:`switch.api.community.controllers.GroupController.create_group`.
        """
        return await self.community_service.groups.create_group(group)

    async def update_group(self: "swibots.ApiClient", group: Group) -> str:
        """Update group

        Args:
            :obj:`swibots.api.community.models.Group`: The group object.

        Returns:
            str:  group id

        Raises:
            :obj:`switch.error.SwitchError`: If the group could not be retrieved

        This method does the same as :meth:`switch.api.community.controllers.GroupController.update_group`.
        """
        return await self.community_service.groups.update_group(group)

    async def delete_group(self: "swibots.ApiClient", id: str) -> bool:
        """Delete group

        Args:
            :obj:`swibots.api.community.models.Group`: The group object.

        Returns:
            bool: Whether the group was deleted!

        Raises:
            :obj:`switch.error.SwitchError`: If the group could not be retrieved

        This method does the same as :meth:`switch.api.community.controllers.GroupController.delete_group`.
        """
        return await self.community_service.groups.delete_group(id)
