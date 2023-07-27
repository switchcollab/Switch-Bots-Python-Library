from typing import List
import swibots
from swibots.api.chat.models import GroupChatHistory


class GetChannelChatHistory:
    async def get_channel_chat_history(
        self: "swibots.ApiClient",
        channel_id: str,
        community_id: str,
        user_id: int = None,
        page_limit: int = 100,
        page_offset=0,
    ) -> GroupChatHistory:
        """Get channel chat history


        Parameters:
            channel_id (``int``): The channel id
            limit (``int``, *optional*): The maximum number of messages to return. Defaults to 100.
            offset (``int``, *optional*): The offset. Defaults to 0.
            community_id (``int``): The community id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.GroupChatHistory]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved
        """
        return await self.chat_service.messages.get_channel_chat_history(
            channel_id, community_id, user_id, page_limit, page_offset
        )
