from typing import List
import swibots
from swibots.api.chat.models import GroupChatHistory


class GetGroupChatHistory:
    async def get_group_chat_history(
        self: "swibots.ApiClient",
        group_id: str,
        community_id: str,
        user_id: int = None,
        page_limit: int = 100,
        page_offset=0,
    ) -> GroupChatHistory:
        """Get group chat history

        Parameters:
            group_id (``int``): The group id
            limit (``int``, *optional*): The maximum number of messages to return. Defaults to 100.
            offset (``int``, *optional*): The offset. Defaults to 0.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved

        This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_group_chat_history`.
        """
        return await self.chat_service.messages.get_group_chat_history(
            group_id, community_id, user_id, page_limit, page_offset
        )
