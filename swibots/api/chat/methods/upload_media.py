from typing import TYPE_CHECKING, Type, TypeVar, Optional
import swibots
from io import BytesIO
from swibots.api.common.models import Media

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
            path: The path to the file to upload
            caption: str
            description: str
            mime_type: str
            callback: Callable
            callback_args: tuple

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
        document: str | BytesIO,
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
        """Send a media to Chat!

        Arguments:
          message (str): the message
          document (str | BytesIO): file path to upload
          caption (str): the media caption
          description (str): the media description
          thumb (str): file path to use as thumb
          community_id (str): The community ID
          group_id (str) The Group ID
          channel_id (str) Channel ID
          user_id (int) User ID
          blocking (bool): whether to block task
          progress (Callable[function]): Progress callback function.
          progress_args (tuple)

        Returns:
          `Message` | `Task`
        """
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
        """Update Info of uploaded media
        
        media_id: int: Media Id
        caption: str: Caption of media
        description: str: Description of media
        """
        return await self.chat_service.media.update_media(
            media_id=media_id, caption=caption, description=description
        )

    async def delete_media(self: "swibots.ApiClient", media_id: int):
        """Delete existing uploaded media!
        
        Arguments:
          media_id: media id to delete"""
        return await self.chat_service.media.delete_media(media_id)