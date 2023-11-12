from typing import List, Union
import swibots
from swibots.api.chat.models import Message


class GetCommunityMediaFilesByStatus:
    async def get_community_media_files_by_status(
        self: "swibots.ApiClient", status: Union[str, List[str]],
        community_id: str = None,
        group_id: str = None,
        channel_id: str = None,
        user_id: int = None,
    ) -> List[Message]:
        """Get community media files by status

        Parameters:
            community_id (``int``): The community id
            status (``str`` | `List[str]`): The status

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved

        This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_community_media_files_by_status`.
        """
        return await self.chat_service.messages.get_community_media_files_by_status(
            community_id=community_id,
            user_id=user_id,
            channel_id=channel_id,
            group_id=group_id,
            status=status
        )
