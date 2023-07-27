import swibots

from swibots.api.community.models import Community


class GetCommunity:
    async def get_community(self: "swibots.ApiClient", id: str = '', username: str = '') -> Community:
        """Get a community by its ID or username

        Args:
            id (`str`): The ID of the community
            username (`str`): Username of the community

        Returns:
            :obj:`swibots.api.community.models.Community`: The community object.

        Raises:
            :obj:`switch.error.SwitchError`: If the community could not be retrieved
            :obj:`ValueError`: if the community id and username is provided together.

        This method does the same as :meth:`switch.api.community.controllers.CommunityController.get_community`.
        """
        return await self.community_service.communities.get_community(id, username=username)
