import asyncio
import os
import json, mimetypes
import logging
from io import BytesIO
from typing import TYPE_CHECKING, List, Optional

from swibots.utils.types import (
    UploadProgressCallback,
    DownloadProgressCallback,
    ReadCallbackStream,
    IOClient,
    UploadProgress,
)
from swibots.api.common.models import Media

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
        path: str | BytesIO,
        caption: Optional[str] = None,
        description: Optional[str] = None,
        mime_type: Optional[str] = None,
        callback: UploadProgressCallback = None,
        callback_args: Optional[tuple] = None,
    ) -> Media:
        """upload media from path"""

        url = f"{BASE_PATH}/upload-multipart"
        if isinstance(path, BytesIO):
            file_name = path.name
        else:
            file_name = path

        if not mime_type:
            mime_type = mimetypes.guess_type(file_name)[0] or "application/octet-stream"

        form_data = {
            "caption": caption,
            "description": description,
            "mimeType": mime_type
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

    async def delete_media(self, media_id: int):
        await self.client.delete(
            "/v1/community/channel/media", data={"mediaId": media_id}
        )
        return True

    async def download_by_media_id(
        self,
        media_id: int,
        file_name: str = None,
        in_memory: Optional[bool] = False,
        block: Optional[bool] = True,
        progress: Optional[DownloadProgressCallback] = None,
        progress_args: Optional[tuple] = (),
    ):
        url = f"{BASE_PATH}/{media_id}/download"
        return await self.client.app.handle_download(
            url,
            file_name=file_name,
            in_memory=in_memory,
            block=block,
            progress=progress,
            progress_args=progress_args,
        )
