from typing import TYPE_CHECKING, Type, TypeVar, Optional
import swibots
from swibots.api.common.models import Media
from swibots.api.common.models import MediaUploadRequest

if TYPE_CHECKING:
    from swibots.api import ApiClient


class UploadMedia:
    async def upload_media(
        self: "ApiClient",
        path: str,
        caption: Optional[str] = None,
        description: Optional[str] = None,
        mime_type: Optional[str] = None,
        callback: callable = None,
        callback_args: tuple = None,
    ) -> Media:
        """upload a file to get `Media` object.

        Arguments:
        path: The path to the file to upload, or a MediaUploadRequest object.

        Returns:
        A Media object representing the uploaded file.
        """
        return await self.chat_service.media.upload_media(
            path,
            caption=caption,
            description=description,
            mime_type=mime_type,
            callback=callback,
            callback_args=callback_args,
        )

    async def send_media(
        self: "swibots.ApiClient",
        document: str,
        message: Optional[str] = None,
        community_id: Optional[str] = None,
        group_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        user_id: Optional[int] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        thumb: Optional[str] = None,
        reply_to_message_id: Optional[int] = None,
        blocking: Optional[bool] = True,
        progress: Optional[callable] = None,
        progress_args: Optional[tuple] = None,
        **kwargs,
    ):
        return await self.chat_service.messages.send_media(
            document=document,
            message=message,
            community_id=community_id,
            group_id=group_id,
            channel_id=channel_id,
            user_id=user_id,
            caption=caption,
            description=description,
            file_name=file_name,
            mime_type=mime_type,
            thumb=thumb,
            blocking=blocking,
            progress=progress,
            progress_args=progress_args,
            reply_to_message_id=reply_to_message_id,
            **kwargs,
        )

    async def update_media_info(
        self: "swibots.ApiClient",
        media_id: int,
        caption: Optional[str] = None,
        description: Optional[str] = None,
    ):
        """Update Info of uploaded media"""
        return await self.chat_service.media.update_media(
            media_id=media_id, caption=caption, description=description
        )
