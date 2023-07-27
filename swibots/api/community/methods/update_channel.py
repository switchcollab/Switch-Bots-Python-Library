import swibots

from swibots.api.community.models import Channel


class UpdateChannel:
    async def update_channel(self: "swibots.ApiClient", channel: Channel) -> str:
        """Update channel

        Args:
            :obj:`swibots.api.community.models.Channel`: The channel object.

        Returns:
            str:  channel id

        Raises:
            :obj:`switch.error.SwitchError`: If the channel could not be retrieved

        This method does the same as :meth:`switch.api.community.controllers.ChannelController.update_channel`.
        """
        return await self.community_service.channels.update_channel(channel)
