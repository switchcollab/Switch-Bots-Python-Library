import asyncio
import os
import json, mimetypes
import logging
from typing import TYPE_CHECKING, List, Optional

from swibots.utils.types import (
    UploadProgressCallback,
    ReadCallbackStream,
    IOClient,
    UploadProgress,
)
from swibots.api.common.models import User, MediaUploadRequest, Media
from swibots.api.community.models import Channel, Group

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/media"


class MediaController:
    """Media controller
    This controller is used to communicate with the media endpoints.
    """

    def __init__(self, client: "ChatClient"):
        self.client = client

    async def upload_media(
        self,
        path: str,
        caption: Optional[str] = None,
        description: Optional[str] = None,
        mime_type: Optional[str] = None,
        callback: UploadProgressCallback = None,
        callback_args: Optional[tuple] = None,
    ) -> Media:
        """upload media from path or with MediaUploadRequest"""

        url = f"{BASE_PATH}/upload-multipart"
        form_data = {
            "caption": caption,
            "description": description,
            "mimeType": mime_type
            or mimetypes.guess_type(path)[0]
            or "application/octet-stream",
        }

        reader = ReadCallbackStream(path, None)
        if callback:
            d_progress = UploadProgress(
                current=0,
                readed=0,
                file_name=path,
                client=IOClient(),
                url=url,
                callback=callback,
                callback_args=callback_args,
            )
            reader.callback = d_progress.update
            d_progress._readable_file = reader
        files = {"file": (path, reader, mime_type)}

        response = await self.client.post(BASE_PATH, form_data=form_data, files=files)
        reader.close()

        return self.client.build_object(Media, response.data)

    async def update_media(
        self,
        media_id: int,
        caption: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Media:
        response = await self.client.put(
            BASE_PATH,
            data={"id": media_id, "caption": caption, "description": description},
        )
        return self.client.build_object(Media, response.data)
