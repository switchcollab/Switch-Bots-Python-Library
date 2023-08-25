from typing import TYPE_CHECKING, Type, TypeVar, Optional
import swibots
from swibots.api.chat.models import Message, InlineMarkup
from swibots.api.common.models import MediaUploadRequest, EmbeddedMedia

if TYPE_CHECKING:
    from swibots.api import ApiClient


class SendMessage:
    async def send_message(
        self: "ApiClient",
        message: str,
        community_id: str = None,
        channel_id: str = None,
        group_id: str = None,
        user_id: Optional[int] = None,
        embed_message: Optional[EmbeddedMedia] = None,
        inline_markup: Optional[InlineMarkup] = None,
        reply_to_message_id: Optional[int] = None,
        **kwargs,
    ) -> Message:
        """Send a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to send

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent

        This functions does the same as :meth:`~switch.api.chat.controllers.MessageController.send_message`.
        """
        return await self.chat_service.messages.send_message(
            message,
            community_id=community_id,
            group_id=group_id,
            channel_id=channel_id,
            user_id=user_id,
            embed_message=embed_message,
            inline_markup=inline_markup,
            reply_to_message_id=reply_to_message_id,
            **kwargs,
        )
