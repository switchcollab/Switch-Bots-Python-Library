from typing import TYPE_CHECKING, Type, TypeVar, Optional, Tuple
import swibots
from swibots.api.chat.models import Message, InlineMarkup
from swibots.api.common.models import EmbeddedMedia

if TYPE_CHECKING:
    from swibots.api import ApiClient


class EditMessage:
    async def edit_message(
        self: "ApiClient",
        message_id: int,
        text: str,
        embed_message: EmbeddedMedia = None,
        inline_markup: InlineMarkup = None,
        **kwargs
    ) -> Message:
        """Edit a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to edit

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be edited

        This method does the same as :meth:`~switch.api.chat.controllers.MessageController.edit_message`.
        """
        return await self.chat_service.messages.edit_message(
            message_id=message_id,
            text=text,
            embed_message=embed_message,
            inline_markup=inline_markup,
            **kwargs
        )

    edit_message_text = edit_message

    async def edit_media(
        self: "swibots.ApiClient",
        message_id: Optional[int] = None,
        media_id: Optional[int] = None,
        message: Optional[str] = None,
        document: Optional[str] = None,
        thumb: Optional[str] = None,
        inline_markup: InlineMarkup = None,
        progress=None,
        progress_args: Optional[Tuple] = None,
        mime_type: Optional[str] = None,
        file_name: Optional[str] = None,
    ) -> Message:
        """Edit media of message

        Args:
            message_id (Optional[int], optional): message id to edit
            media_id (Optional[int], optional): media id to update
            message (Optional[str], optional): message or caption
            document (Optional[str], optional): path to new media
            thumb (Optional[str], optional): thumbnail path
            inline_markup (InlineMarkup, optional):
            progress (_type_, optional): progress callback
            progress_args (Optional[Tuple], optional): progress callback args
            mime_type (Optional[str], optional): mime type of file
            file_name (Optional[str], optional): file name

        Returns:
            Media
        """
        return await self.chat_service.messages.edit_media(
            message_id=message_id,
            media_id=media_id,
            message=message,
            progress=progress,
            progress_args=progress_args,
            inline_markup=inline_markup,
            file_name=file_name,
            mime_type=mime_type,
            thumb=thumb,
            document=document,
        )
