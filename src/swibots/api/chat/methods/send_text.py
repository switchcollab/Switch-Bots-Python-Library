from typing import TYPE_CHECKING, Optional, Type, TypeVar
import swibots
from swibots.api.chat.models import Message, InlineMarkup
from swibots.api.community.models import Channel, Group
from swibots.api.common.models import User
from swibots.api.common.models import MediaUploadRequest

if TYPE_CHECKING:
    from swibots.api import ApiClient


class SendText:
    async def send_text(self: "ApiClient", text: str, to: Optional[int | User] = None, channel: Optional[Channel | str] = None, group: Optional[Group | str] = None,  inline_markup: InlineMarkup = None, media: MediaUploadRequest = None) -> Message:
        """Send a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to send

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent

        This functions does the same as :meth:`~switch.api.chat.controllers.MessageController.send_message`.
        """
        return await self.chat_service.messages.send_text(text, to, channel, group, inline_markup, media)
