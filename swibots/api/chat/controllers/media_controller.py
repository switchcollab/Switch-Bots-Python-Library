import asyncio
import os
import json, mimetypes
import logging, base64
from io import BytesIO
import json, mimetypes
import logging, hashlib
from io import BytesIO
import uuid
from httpx import AsyncClient
from typing import TYPE_CHECKING, List, Optional

from swibots.utils.types import (
    UploadProgressCallback,
    DownloadProgressCallback,
    IOClient,
    UploadProgress,
)
from swibots.config import APP_CONFIG
from swibots.api.common.models import Media


if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logger = logging.getLogger(__name__)

BASE_PATH = "/v1/media"

api_url = "https://api004.backblazeb2.com"

account_id = APP_CONFIG["BACKBLAZE"].get("ACCOUNT_ID")
application_key = APP_CONFIG["BACKBLAZE"].get("APPLICATION_KEY")

bucket_id = APP_CONFIG["BACKBLAZE"].get("BUCKET_ID")

headers = {}
headers["Authorization"] = (
    "Basic " + base64.b64encode(f"{account_id}:{application_key}".encode()).decode()
)
headers["accept"] = "application/json"


class MediaController:
    """Media controller
    This controller is used to communicate with the media endpoints.
    """

    def __init__(self, client: "ChatClient"):
        self.client = client
        self.__token = None
        self._client = AsyncClient(timeout=None, verify=False)

    async def getAccountInfo(self):
        if self.__token:
            return
        response = await self._client.get(
            "https://api.backblazeb2.com/b2api/v2/b2_authorize_account", headers=headers
        )
        data = response.json()
        if token := data.get("authorizationToken"):
            self.__token = token
        return data

    async def file_to_response(self, path, mime_type=None, file_name=None):
        await self.getAccountInfo()
        Isbytes = isinstance(path, BytesIO)

        if not mime_type:
            mime_type = mimetypes.guess_type(path.name if Isbytes else path)[0] or "application/octet-stream"

        head = {
            "Content-Type": "application/json",
            "Authorization": self.__token,
        }
        rsp = await self._client.get(
            f"https://api004.backblazeb2.com/b2api/v2/b2_get_upload_url?bucketId={bucket_id}",
            headers=head,
        )

        token = rsp.json()["authorizationToken"]
        if Isbytes:
            file_source = path
        else:
            file_source = open(path, "rb")

        with file_source as f:
            content = f.read()
            file_sha1 = hashlib.sha1(content).hexdigest()
            headers = {
                "Authorization": token,
                "X-Bz-File-Name": file_name,
                "Content-Type": mime_type,
                "X-Bz-Content-Sha1": file_sha1,
            }
            rsp = await self._client.post(
                rsp.json()["uploadUrl"],
                headers=headers,
                data=content,
            )
            file_response = rsp.json()
            return file_response

    async def file_to_url(self, path, mime_type: str = None, *args, **kwargs) -> str:
        if path:
            _, ext = os.path.splitext(path)
            file_name = f"{uuid.uuid1()}{ext}"

            file = await self.file_to_response(path, mime_type, file_name)
            return f"https://f004.backblazeb2.com/file/switch-bucket/{file['fileName']}"

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
        part_size: int = 10 * 1024 * 1024,
        task_count: int = 20,
        min_file_size: int = 10 * 1024 * 1024,
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
        _is_bytesio = isinstance(path, BytesIO)
    
        if not _is_bytesio:
            size = os.path.getsize(path)
        else:
            size = len(path.getvalue())

        _, ext = os.path.splitext(path.name if _is_bytesio else path)
        file_name = f"{uuid.uuid1()}{ext}"

        if size > min_file_size and not (size / part_size) < 2:
            file_response = await self.upload_large_file(
                path,
                callback=callback,
                content_type=mime_type,
                file_name=file_name,
                callback_args=callback_args,
                part_size=part_size,
                task_count=task_count,
                file_size=size
            )
        else:
            file_response = await self.file_to_response(path, mime_type, file_name)

        url = f"https://f004.backblazeb2.com/file/switch-bucket/{file_response['fileName']}"

        media = {
            "caption": caption,
            "description": description,
            "mimeType": mime_type,
            "fileSize": file_response.get("size", size),
            "fileName": file_response["fileName"],
            "downloadUrl": url,
            "thumbnailUrl": await self.file_to_url(thumb) or url,
            "mediaType": media_type,
            "sourceUri": file_response["fileId"],
            "checksum": file_response["contentSha1"],
        }
        return self.client.build_object(Media, media)

    async def __upload_file(
        self,
        token,
        part_number,
        chunk,
        fileId: str,
        progress: UploadProgress,
        partHash: dict,
    ):
        sha1_checksum = hashlib.sha1(chunk).hexdigest()

        respp = await self._client.post(
            f"https://api004.backblazeb2.com/b2api/v2/b2_get_upload_part_url",
            json={"fileId": fileId},
            headers={"Authorization": token},
        )
        if respp.status_code != 200:
            logger.error("on Part url")
            logger.error(respp.json())
        token = respp.json()["authorizationToken"]
        upload_part_url = respp.json()["uploadUrl"]

        respp = await self._client.post(
            upload_part_url,
            data=chunk,
            headers={
                "Authorization": token,
                "X-Bz-Part-Number": str(part_number),
                "X-Bz-Content-Sha1": sha1_checksum,
            },
        )
        if respp.status_code != 200:
            logger.error("onUpload")
            logger.error(respp.json())
        hash = respp.json()["contentSha1"]
        partHash[hash] = respp.json()["partNumber"]
        await progress.bytes_readed(respp.json()["contentLength"])

    async def upload_large_file(
        self,
        path: str | BytesIO,
        callback,
        content_type,
        file_name,
        file_info=None,
        callback_args=None,
        part_size=None,
        task_count=None,
        file_size=None
    ):
        await self.getAccountInfo()

        client = IOClient()
        progress = UploadProgress(
            path=path, callback=callback, callback_args=callback_args, client=client,
            size=file_size
        )
        if isinstance(path, BytesIO):
            file_source = path
            if not file_name:
                file_name = path.name
        else:
            file_source = open(path, "rb")
    
        with file_source as file:
            head = {
                "Content-Type": content_type,
                "X-Bz-File-Name": file_name,
                "Authorization": self.__token,
            }
            data = {
                "fileName": file_name,
                "contentType": content_type,
                "bucketId": bucket_id,
                "fileInfo": file_info,
            }
            partHash = {}
            logger.info("start large file")
            respp = await self._client.post(
                "https://api004.backblazeb2.com/b2api/v2/b2_start_large_file",
                headers=head,
                data=json.dumps(data),
            )
            if respp.status_code != 200:
                logger.error("on large file")
                logger.error(respp.json())

            logger.debug(respp.json())

            fileId = respp.json()["fileId"]
            part_number = 1
            tasks = []
            while True:
                chunk = file.read(part_size)
                if not chunk:
                    break

                tsk = asyncio.create_task(
                    self.__upload_file(
                        self.__token, part_number, chunk, fileId, progress, partHash
                    )
                )
                tasks.append(tsk)
                if len(tasks) == task_count:
                    await asyncio.gather(*tasks)
                    tasks.clear()

                part_number += 1
        if tasks:
            await asyncio.gather(*tasks)
        hashes = list(map(lambda x: x[0], sorted(partHash.items(), key=lambda x: x[1])))

        response = await self._client.post(
            f"https://api004.backblazeb2.com/b2api/v2/b2_finish_large_file",
            json={
                "fileId": fileId,
                "partSha1Array": hashes,
            },
            headers={"Authorization": self.__token},
        )
        if response.status_code != 200:
            logger.error(response.json())

        return response.json()

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
