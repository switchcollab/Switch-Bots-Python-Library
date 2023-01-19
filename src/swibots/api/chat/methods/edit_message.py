from typing import Type, TypeVar
import swibots
from swibots.api.chat.models import Message


class EditMessage:
    async def edit_message(self: "swibots.ApiClient", message: Message) -> Message:
        """Edit a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to edit

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be edited

        This method does the same as :meth:`~switch.api.chat.controllers.MessageController.edit_message`.
        """
        return await self.chat_service.messages.edit_message(message)
