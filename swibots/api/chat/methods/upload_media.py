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
        media: Optional[Media] = None,
        message: Optional[str] = None,
        community_id: Optional[str] = None,
        group_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        user_id: Optional[int] = None,
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        thumb: Optional[str] = None,
        blocking: Optional[bool] = True,
        progress: Optional[callable] = None,
        progress_args: Optional[tuple] = None,
        **kwargs,
    ):
        return await self.chat_service.messages.send_media(
            document,
            media,
            message,
            community_id,
            group_id,
            channel_id,
            user_id,
            caption,
            file_name,
            mime_type,
            thumb,
            blocking,
            progress,
            progress_args,
            **kwargs,
        )
