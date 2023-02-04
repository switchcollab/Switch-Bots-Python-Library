import swibots

from swibots.api.community.models import Community


class GetCommunity:
    async def get_community(self: "swibots.ApiClient", id: str) -> Community:
        """Get a community by its ID

        Args:
            id (`str`): The ID of the community

        Returns:
            :obj:`swibots.api.community.models.Community`: The community object.

        Raises:
            :obj:`switch.error.SwitchError`: If the community could not be retrieved

        This method does the same as :meth:`switch.api.community.controllers.CommunityController.get_community`.
        """
        return await self.community_service.communities.get_community(id)
