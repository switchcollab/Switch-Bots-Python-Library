from typing import List
import swibots
from swibots.api.chat.models import Message


class GetMessage:
    async def get_message(self: "swibots.ApiClient", message_id: int) -> Message:
        """Get a message

        Parameters:
            message_id (``int``): The message id

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be retrieved

        This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_message`.
        """
        return await self.chat_service.messages.get_message(message_id)
