from typing import List
import swibots
from swibots.api.chat.models import Message


class GetMessages:
    async def get_messages(
        self: "swibots.ApiClient", user_id: int, limit: int = 100, offset: int = 0
    ) -> List[Message]:
        """Get messages

        Parameters:
            user_id (``int``, *optional*): The user id.
            limit (``int``, *optional*): The limit of messages to retrieve. Defaults to 100.
            offset (``int``, *optional*): The offset of messages to retrieve. Defaults to 0

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved

        This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_messages`.
        """
        return await self.chat_service.messages.get_messages(
            user_id, limit=limit, offset=offset
        )
