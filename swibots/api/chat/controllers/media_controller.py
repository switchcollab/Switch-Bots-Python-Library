import asyncio
import os
import json, mimetypes
import logging
from io import BytesIO
from typing import TYPE_CHECKING, List, Optional

from swibots.utils.types import (
    UploadProgressCallback,
    DownloadProgressCallback,
    IOClient,
    UploadProgress,
)
from swibots.config import APP_CONFIG
from swibots.api.common.models import Media
from b2sdk.v2 import B2Api

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
        self.backblaze = B2Api()
        self.bucket = None
        if (account_id := APP_CONFIG["BACKBLAZE"].get("ACCOUNT_ID")) and (
            application_key := APP_CONFIG["BACKBLAZE"].get("APPLICATION_KEY")
        ):
            self.backblaze.authorize_account("production", account_id, application_key)
        self.prepare_bucket()

    def prepare_bucket(self):
        if (
            bucket_id := APP_CONFIG["BACKBLAZE"].get("BUCKET_ID")
        ) and self.backblaze.get_account_id():
            self.bucket = self.backblaze.get_bucket_by_id(bucket_id)

    def file_to_url(self, path, mime_type: str = None, *args, **kwargs) -> str:
        if path:
            file = self.bucket.upload_local_file(
                path, path, content_type=mime_type, *args, **kwargs
            ).as_dict()
            return self.backblaze.download_file_by_id(file["fileId"])

    async def upload_media(
        self,
        path: str | BytesIO,
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        description: Optional[str] = None,
        thumb: Optional[str] = None,
        mime_type: Optional[str] = None,
        media_type: Optional[int] = None,
        callback: UploadProgressCallback = None,
        callback_args: Optional[tuple] = None,
    ) -> Media:
        """upload media from path"""
        if not file_name:
            if isinstance(path, BytesIO):
                file_name = path.name
            else:
                file_name = path

        if not mime_type:
            mime_type = mimetypes.guess_type(file_name)[0] or "application/octet-stream"

        log.debug(f"Sending request to backblaze: {path}")

        file_response = self.bucket.upload_local_file(
            path,
            file_name=file_name,
            content_type=mime_type,
            progress_listener=UploadProgress(
                path,
                callback=callback,
                callback_args=callback_args,
            )
            if callback
            else None,
        ).as_dict()

        url = self.backblaze.get_download_url_for_fileid(file_response["fileId"])
        media = {
            "caption": caption,
            "description": description,
            "mimeType": mime_type,
            "fileSize": file_response["size"],
            "fileName": file_response["fileName"],
            "downloadUrl": url,
            "thumbnailUrl": self.file_to_url(thumb) if thumb != path else url,
            "mediaType": media_type,
            "sourceUri": file_response["fileId"],
            "checksum": file_response["contentSha1"],
        }

        return self.client.build_object(Media, media)

    async def get_media(self, media_id: int) -> Media:
        response = await self.client.get(f"{BASE_PATH}/{media_id}")
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
