from typing import TYPE_CHECKING, Type, TypeVar
import swibots
from swibots.api.chat.models import Message
from swibots.api.common.models import MediaUploadRequest, EmbeddedMedia

if TYPE_CHECKING:
    from swibots.api import ApiClient


class ReplyMessage:
    async def reply_message(self: "swibots.ApiClient", message: int | Message, reply: Message, media: MediaUploadRequest | EmbeddedMedia = None) -> Message:
        """Send a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to send

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent

        This functions does the same as :meth:`~switch.api.chat.controllers.MessageController.send_message`.
        """
        return await self.chat_service.messages.reply(message, reply, media)
