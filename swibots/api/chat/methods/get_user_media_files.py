from typing import List
import swibots
from swibots.api.chat.models import Message


class GetUserMediaFiles:
    async def get_user_media_files(
        self: "swibots.ApiClient",
        user_id: int = None,
    ) -> List[Message]:
        """Get user media files


        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The user media files

        Raises:
            ``~switch.error.SwitchError``: If the user media files could not be retrieved

        This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_user_media_files`.
        """
        return await self.chat_service.messages.get_user_media_files(user_id)
