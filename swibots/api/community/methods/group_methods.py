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
