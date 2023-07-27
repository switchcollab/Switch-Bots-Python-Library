from typing import Type, TypeVar
import swibots
from swibots.api.chat.models import Message


class DeleteMessage:
    async def delete_message(self: "swibots.ApiClient", message: int | Message) -> bool:
        """Delete a message

        Parameters:
            message (``int`` | ``~switch.api.chat.models.Message``): The message to delete

        Returns:
            ``bool``: Whether the message was deleted

        Raises:
            ``~switch.error.SwitchError``: If the message could not be deleted

        This method does the same as :meth:`~switch.api.chat.controllers.MessageController.delete_message`.
        """
        return await self.chat_service.messages.delete_message(message)
