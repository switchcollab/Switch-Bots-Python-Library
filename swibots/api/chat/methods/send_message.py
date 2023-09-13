from typing import TYPE_CHECKING, Optional
import swibots
from swibots.api.chat.models import Message, InlineMarkup
from swibots.api.common.models import EmbeddedMedia

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
        user_session_id: Optional[str] = None,
        document: Optional[str] = None,
        caption: Optional[str] = None,
        description: Optional[str] = None,
        embed_message: Optional[EmbeddedMedia] = None,
        inline_markup: Optional[InlineMarkup] = None,
        reply_to_message_id: Optional[int] = None,
        **kwargs,
    ) -> Message:
        """Send a message

        Parameters:
            `message`: text to send as message
            `community_id`: Community ID
            `group_id`: Group id
            `channel_id`: Channel ID
            `user_id`: User id to send message
            `user_session_id`: Session ID, present if bot is added as channel in the community.
            ``

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent
            ``~ValueError``: If Chat I
        """
        return await self.chat_service.messages.send_message(
            message,
            community_id=community_id,
            group_id=group_id,
            channel_id=channel_id,
            user_id=user_id,
            user_session_id=user_session_id,
            document=document,
            description=description,
            caption=caption,
            embed_message=embed_message,
            inline_markup=inline_markup,
            reply_to_message_id=reply_to_message_id,
            **kwargs,
        )
