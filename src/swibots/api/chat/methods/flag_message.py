from typing import Type, TypeVar
import swibots
from swibots.api.chat.models import Message


class FlagMessage:
    async def flag_message(self: "swibots.ApiClient", message: Message | int) -> bool:
        """Flag a message

        Parameters:
            message (``~switch.api.chat.models.Message`` | ``int``): The message to flag

        Returns:
            ``bool``: True if the message was flagged

        Raises:
            ``~switch.error.SwitchError``: If the message could not be flagged

        This method does the same as :meth:`~switch.api.chat.controllers.MessageController.flag_message`.
        """
        return await self.chat_service.messages.flag_message(message)
