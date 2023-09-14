import swibots
from typing import List

from swibots.api.community.models import Channel


class ChannelMethods:
    async def create_channel(self: "swibots.ApiClient", channel: Channel) -> str:
        """Create channel

        Args:
            :obj:`swibots.api.community.models.Channel`: The channel object.

        Returns:
            str:  channel id

        Raises:
            :obj:`switch.error.SwitchError`: If the channel could not be retrieved

        This method does the same as :meth:`switch.api.community.controllers.ChannelController.create_channel`.
        """
        return await self.community_service.channels.create_channel(channel)

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

    async def get_all_channels(
        self: "swibots.ApiClient", community_id: str
    ) -> List[Channel]:
        """
        Get all channels from the community.
        """
        return await self.community_service.channels.get_all_channels(community_id)

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
