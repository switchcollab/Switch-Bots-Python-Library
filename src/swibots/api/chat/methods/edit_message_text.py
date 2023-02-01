from typing import TYPE_CHECKING, Type, TypeVar
import swibots
from swibots.api.chat.models import Message, InlineMarkup

if TYPE_CHECKING:
    from swibots.api import ApiClient


class EditMessageText:
    async def edit_message_text(self: "ApiClient", message: int | Message, text: str, inline_markup: InlineMarkup = None) -> Message:
        """Send a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to send

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent

        This functions does the same as :meth:`~switch.api.chat.controllers.MessageController.send_message`.
        """
        return await self.chat_service.messages.edit_message_text(message, text, inline_markup)
