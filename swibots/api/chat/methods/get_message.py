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

    async def get_messages(
        self: "swibots.ApiClient", message_ids: List[int] | int
    ) -> Message | List[Message]:
        """Get messages by ids"""
        if isinstance(message_ids, list):
            return [await self.get_message(id) for id in message_ids]
        return await self.get_message(message_ids)
