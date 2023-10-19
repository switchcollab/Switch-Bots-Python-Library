import asyncio
import os
import json, mimetypes
import logging
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
from b2sdk.v2 import B2Api

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logger = logging.getLogger(__name__)

BASE_PATH = "/v1/media"

headers = {}
headers["Authorization"] = (
    "Basic "
    + "MDA0YjRjZjkwNDFiOWYxMDAwMDAwMDAwNjpLMDA0Zi9BN1FtSkppUW1NWnN5VzN5R3ZoVmNJd2Q0"
)
headers["accept"] = "application/json"


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
        self.backblaze = B2Api()
        self.bucket = None
        if (account_id := APP_CONFIG["BACKBLAZE"].get("ACCOUNT_ID")) and (
            application_key := APP_CONFIG["BACKBLAZE"].get("APPLICATION_KEY")
        ):
            self.backblaze.authorize_account("production", account_id, application_key)
        self.prepare_bucket()
        self.__token = None
        self._client = AsyncClient(timeout=None, verify=False)
    
    async def getAccountInfo(self):
        response = await self._client.get(
            "https://api.backblazeb2.com/b2api/v2/b2_authorize_account", headers=headers
        )
        data = response.json()
        if token := data.get("authorizationToken"):
            self.__token = token
        return data
    
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
            return self.backblaze.get_download_url_for_fileid(file["fileId"])

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
        _part_size: int = 100*1024*1024,
        _task_count: int = 20
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

        size = os.path.getsize(path)

        async def upload_large_file(self, content_type, file_name, file_info=None):
            if not self.__token:
                info = await self.getAccountInfo()
            client = IOClient()
            progress = UploadProgress(
                path=path,
                callback=callback,
                callback_args=callback_args
            ,
            client=client
            )
            with open(path, "rb") as file:
                head = {
                    "Content-Type": content_type,
                    "X-Bz-File-Name": file_name,
                    "Authorization": self.__token,
                }
                data = {
                    "fileName": file_name,
                    "contentType": content_type,
                    "bucketId": "6b741c0f098034a18b190f11",
                    "fileInfo": file_info
                    #            "fileInfo": {"large_file_sha1": file_sha1},
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

                logger.info(respp.json())
                #       token= respp.json()["authorizationToken"]
                fileId = respp.json()["fileId"]
                part_number = 1
                tasks = []
                while True:
                    chunk = file.read(_part_size)
                    if not chunk:
                        break

                    async def uploadFile(token, part_number, chunk):
                        sha1_checksum = hashlib.sha1(chunk).hexdigest()

    #                    logger.info("get part url")
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
                        # (respp.json(), token)
    #                    logger.info("calling upload")
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
    #                    logger.info(respp.json())
                        hash = respp.json()["contentSha1"]
                        partHash[hash] = respp.json()["partNumber"]
                        await progress.bytes_readed(respp.json()["contentLength"])

                    tsk = asyncio.create_task(
                        uploadFile(self.__token, part_number, chunk)
                    )
                    tasks.append(tsk)
                    if len(tasks) == _task_count:
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



        if not mime_type:
            mime_type = mimetypes.guess_type(file_name)[0] or "application/octet-stream"
        

        log.debug(f"Sending request to backblaze: {path}")

        _, ext = os.path.splitext(path)
        file_name = f"{uuid.uuid1()}{ext}"
        if size > 100 * 1024 * 1024: 
            file_response = await upload_large_file(self, mime_type, file_name)
        else:
            _progress = UploadProgress(
                path,
                callback=callback,
                callback_args=callback_args,
             #   loop=self.loop,
            )
            loop = asyncio.get_event_loop()
            file_response = await loop.run_in_executor(None, lambda: self.bucket.upload_local_file(
                    path,
                    file_name=file_name,
                    content_type=mime_type,
                    progress_listener=_progress if callback else None,
                ).as_dict())

        url = self.backblaze.get_download_url_for_fileid(file_response["fileId"])

        media = {
            "caption": caption,
            "description": description,
            "mimeType": mime_type,
            "fileSize": file_response.get("size", size),
            "fileName": file_response["fileName"],
            "downloadUrl": url,
            "thumbnailUrl": self.file_to_url(thumb) or url,
            "mediaType": media_type,
            "sourceUri": file_response["fileId"],
            "checksum": file_response["contentSha1"],
        }
        print(media)
        return self.client.build_object(Media, media)
        

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
