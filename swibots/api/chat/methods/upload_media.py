from typing import TYPE_CHECKING, Type, TypeVar
import swibots
from swibots.api.common.models import Media
from swibots.api.common.models import MediaUploadRequest

if TYPE_CHECKING:
    from swibots.api import ApiClient


class UploadMedia:
    async def upload_media(self: "ApiClient", path: str | MediaUploadRequest) -> Media:
        """upload a file to get `Media` object.

        Arguments:
        path: The path to the file to upload, or a MediaUploadRequest object.

        Returns:
        A Media object representing the uploaded file.
        """
        return await self.chat_service.media.upload_media(path)