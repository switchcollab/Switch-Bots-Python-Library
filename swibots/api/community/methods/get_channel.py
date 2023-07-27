import swibots

from swibots.api.community.models import Channel


class GetChannel:
    async def get_channel(self: "swibots.ApiClient", id: str) -> Channel:
        """Get a community by its ID

        Args:
            id (`str`): The ID of the channel

        Returns:
            :obj:`swibots.api.community.models.Channel`: The channel object.

        Raises:
            :obj:`switch.error.SwitchError`: If the channel could not be retrieved

        This method does the same as :meth:`switch.api.community.controllers.ChannelController.get_channel`.
        """
        return await self.community_service.channels.get_channel(id)
