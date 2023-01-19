from typing import Type, TypeVar
import swibots
from swibots.api.chat.models import Message


class SendMessage:
    async def send_message(self: "swibots.ApiClient", message: Message) -> Message:
        """Send a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to send

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent

        This functions does the same as :meth:`~switch.api.chat.controllers.MessageController.send_message`.
        """
        return await self.chat_service.messages.send_message(message)
