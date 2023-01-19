from typing import List
import swibots
from swibots.api.chat.models import Message


class GetCommunityMediaFiles:
    async def get_community_media_files(
        self: "swibots.ApiClient", community_id: str
    ) -> List[Message]:
        """Get community media files

        Parameters:
            community_id (``int``): The community id

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved

        This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_messages`.
        """
        return await self.chat_service.messages.get_messages(community_id)
