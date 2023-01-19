from typing import List
import swibots
from swibots.api.chat.models import Message


class GetCommunityMediaFilesByStatus:
    async def get_community_media_files_by_status(
        self: "swibots.ApiClient", community_id: str, status: str
    ) -> List[Message]:
        """Get community media files by status

        Parameters:
            community_id (``int``): The community id
            status (``str``): The status

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved

        This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_community_media_files_by_status`.
        """
        return await self.chat_service.messages.get_community_media_files_by_status(
            community_id, status
        )
