import asyncio
import os, tempfile
import json, mimetypes
from datetime import datetime
import logging, base64
from io import BytesIO
import json, mimetypes
import logging, hashlib
from uuid import uuid1
from typing import Union, Dict
from io import BytesIO
import uuid
from httpx import AsyncClient
from typing import TYPE_CHECKING, List, Optional

from swibots.errors import UnknownBackBlazeError
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

MAX_THUMB_SIZE = 1024 * 20


class MediaController:
    """Media controller
    This controller is used to communicate with the media endpoints.
    """

    def __init__(self, client: "ChatClient"):
        self.client = client
        self.__token = None
        self._client = AsyncClient(timeout=None, verify=False)
        self._min_part_size = 5000000

    async def getAccountInfo(self):
        if self.__token:
            return
        response = await self._client.get(
            "https://api.backblazeb2.com/b2api/v2/b2_authorize_account", headers=headers
        )
        data = response.json()
        if token := data.get("authorizationToken"):
            self.__token = token
        log.debug(data)
        self._min_part_size = data.get("absoluteMinimumPartSize")
        return data

    async def file_to_response(
        self,
        path: str | BytesIO,
        mime_type=None,
        file_name=None,
        content: bytes = None,
        callback=None,
        callback_args=None,
        remove: bool = None,
    ):
        await self.getAccountInfo()
        Isbytes = isinstance(path, BytesIO)

        if not mime_type:
            mime_type = (
                mimetypes.guess_type(path.name if Isbytes else path)[0]
                or "application/octet-stream"
            )

        head = {
            "Content-Type": "application/json",
            "Authorization": self.__token,
        }
        rsp = await self._client.get(
            f"https://api004.backblazeb2.com/b2api/v2/b2_get_upload_url?bucketId={bucket_id}",
            headers=head,
        )

        response_data = rsp.json()
        if not response_data.get("authorizationToken"):
            raise UnknownBackBlazeError(response_data)
        token = response_data["authorizationToken"]

        if Isbytes:
            file_source = path
        else:
            file_source = open(path, "rb")

        if not content:
            content = file_source.read()
        else:
            file_source.close()
            if remove:
                os.remove(path)
        file_sha1 = hashlib.sha1(content).hexdigest()

        headers = {
            "Authorization": token,
            "X-Bz-File-Name": file_name,
            "Content-Type": mime_type,
            "X-Bz-Content-Sha1": file_sha1,
            "Content-Length": str(len(content)),
        }

        respp = rsp.json()
        if not response_data.get("uploadUrl"):
            raise UnknownBackBlazeError(respp)

        rsp = await self._client.post(
            respp["uploadUrl"],
            headers=headers,
            data=content,
        )
        file_response = rsp.json()
        if "contentLength" in file_response:
            if callback:
                progress = UploadProgress(
                    path=path,
                    callback=callback,
                    callback_args=callback_args,
                    client=IOClient(),
                )
                await progress.bytes_readed(file_response["contentLength"])
        else:
            log.error(file_response)
        return file_response

    async def generate_from_ffmpeg(self, path: str, hw: int):
        log.debug("checking for ffmpeg")
        ffmpeg_path = os.getenv("FFMPEG_PATH") or "ffmpeg"
        proc = await asyncio.create_subprocess_exec(
            ffmpeg_path, stderr=asyncio.subprocess.PIPE
        )
        await proc.wait()
        if b"ffmpeg version" not in (er := await proc.stderr.read()):
            log.info(f"ffmpeg is not installed, {er}")
            return
        name = os.path.join(tempfile.gettempdir(), f"{uuid1()}.png")
        log.info(f"generating thumb for '{path}'")
        cmd = [
            ffmpeg_path,
            "-i",
            path,
            "-ss",
            "00:00:01.000",
            "-vf",
            f"scale={hw}:-1:force_original_aspect_ratio=increase",
            "-vframes",
            "1",
            name,
        ]
        log.debug(f"Running command, {cmd}")
        proc = await asyncio.create_subprocess_shell(
            " ".join(cmd), stderr=asyncio.subprocess.PIPE
        )
        await proc.wait()
        if os.path.exists(name):
            return name
        log.info(await proc.stderr.read())

    async def get_thumb_url(
        self, path: Union[str, BytesIO], for_document: bool = False, *args, **kwargs
    ) -> str:
        if not path:
            return
        __remove = False
        mime_type = mimetypes.guess_type(path)[0] or "application/octet-stream"
        hw = 30 if for_document else 100
        if "video/" in mime_type:
            path = await self.generate_from_ffmpeg(path, hw)
            if not path:
                return
            __remove = True
        elif not "image/" in mime_type:
            return
        content = None
        if isinstance(path, str):
            size = os.path.getsize(path)
            name = path
        else:
            content = path.getvalue()
            size = len(content)
            name = path.name

        if size > MAX_THUMB_SIZE:
            try:
                from PIL import Image

                log.info(f"creating thumb for {path}")

                img = Image.open(content or path)
                img.thumbnail((hw, hw))
                path = tempfile.gettempdir() + f"/{uuid.uuid1()}.png"
                __remove = True
                img.save(path)
            except ImportError:
                log.warning("thumb size is greater than 20kb, ignoring thumb")
                return

        _, ext = os.path.splitext(name)
        file_name = f"{uuid.uuid1()}{ext}"

        file = await self.file_to_response(
            path, mime_type, file_name, content=content, remove=__remove
        )
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
        auto_thumb: Optional[bool] = True,
        part_size: int = int(os.getenv("UPLOAD_PART_SIZE", 0)),
        task_count: int = int(os.getenv("UPLOAD_TASKS", 0)),
        min_file_size: int = None,
        for_document: bool = False,
    ) -> Media:
        """Upload media to switch

        Args:
            path (str | BytesIO): path to upload
            caption (Optional[str], optional): caption of media Defaults to None.
            description (Optional[str], optional): file name of media. Defaults to None.
            thumb (Optional[str], optional): path to use as thumb for media. Defaults to None.
            mime_type (Optional[str], optional): MIME type of media. Defaults to None.
            media_type (Optional[int], optional): Media type. Defaults to None.
            callback (UploadProgressCallback, optional): Callback progress. Defaults to None.
            callback_args (Optional[tuple], optional): Additional args to use in callbacks. Defaults to None.
            part_size (int, optional): part size while uploading. Defaults to None.
            task_count (int, optional): number of tasks while uploading, Defaults to None.

        Returns:
            Media:
        """

        if not min_file_size:
            min_file_size = self._min_part_size

        if not part_size:
            part_size = self._min_part_size

        if not task_count:
            task_count = 1

        if part_size < self._min_part_size:
            log.warning(
                f"part_size cant be smaller than minimum [{self._min_part_size}]"
            )
            part_size = self._min_part_size

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
            content = path.getvalue()
            size = len(content)
            path = BytesIO(content)

        _, ext = os.path.splitext(path.name if _is_bytesio else path)
        file_name = f"{uuid.uuid1()}{ext}"

        if size > min_file_size and size > self._min_part_size:
            file_response = await self.upload_large_file(
                path,
                callback=callback,
                content_type=mime_type,
                file_name=file_name,
                callback_args=callback_args,
                part_size=part_size,
                task_count=task_count,
                file_size=size,
                file_info={
                    "timestamp": str(datetime.now().timestamp()),
                    "uploaded_by": str(self.client.user.id),
                },
            )
        else:
            file_response = await self.file_to_response(
                path, mime_type, file_name, callback=callback
            )

        url = f"https://f004.backblazeb2.com/file/switch-bucket/{file_response['fileName']}"
        try:
            thumbUrl = await self.get_thumb_url(
                thumb or (path if auto_thumb else None), for_document
            )
        except Exception as er:
            log.exception(er)
            thumbUrl = None

        media = {
            "caption": caption,
            "description": description,
            "mimeType": mime_type,
            "fileSize": file_response.get("size", size),
            "fileName": file_response["fileName"],
            "downloadUrl": url,
            "thumbnailUrl": thumbUrl,
            "mediaType": media_type,
            "sourceUri": file_response["fileId"],
            "checksum": file_response["contentSha1"],
            "ownerId": self.client.app.user.id,
        }
        return self.client.build_object(Media, media)

    async def __upload_file(
        self,
        token,
        part_number,
        chunk,
        fileId: str,
        progress: UploadProgress,
        partHash: Dict,
        retries: int = 1,
    ):
        sha1_checksum = hashlib.sha1(chunk).hexdigest()

        respp = await self._client.post(
            f"https://api004.backblazeb2.com/b2api/v2/b2_get_upload_part_url",
            json={"fileId": fileId},
            headers={"Authorization": token},
        )
        resp_data = respp.json()
        if respp.status_code != 200:
            logger.error("on Part url")
            logger.error(resp_data)

        token = resp_data["authorizationToken"]
        upload_part_url = resp_data["uploadUrl"]
        for _ in range(retries + 1):
            try:
                respp = await self._client.post(
                    upload_part_url,
                    data=chunk,
                    headers={
                        "Authorization": token,
                        "X-Bz-Part-Number": str(part_number),
                        "X-Bz-Content-Sha1": sha1_checksum,
                    },
                )
                resp_data = respp.json()
                if respp.status_code != 200:
                    logger.error("onUpload")
                    logger.error(resp_data)
                break
            except Exception as er:
                log.exception(er)
        hash = resp_data["contentSha1"]
        partHash[hash] = resp_data["partNumber"]
        await progress.bytes_readed(resp_data["contentLength"])

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
        file_size=None,
    ):
        log.info("getting account info")
        await self.getAccountInfo()

        client = IOClient()
        progress = UploadProgress(
            path=path,
            callback=callback,
            callback_args=callback_args,
            client=client,
            size=file_size,
        )
        if isinstance(path, BytesIO) and not file_name:
            file_name = path.name

        with open(path, "rb") if isinstance(path, str) else path as file:
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
                raise UnknownBackBlazeError(respp.json())

            logger.debug(respp.json())

            fileId = respp.json()

            if not fileId.get("fileId"):
                raise UnknownBackBlazeError(fileId)

            fileId = fileId["fileId"]
            part_number = 1
            tasks = []
            while True:
                chunk = file.read(part_size)
                if not chunk:
                    break

                tsk = asyncio.create_task(
                    self.__upload_file(
                        self.__token,
                        part_number,
                        chunk,
                        fileId,
                        progress,
                        partHash,
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
        try:
            response = await self._client.post(
                f"https://api004.backblazeb2.com/b2api/v2/b2_finish_large_file",
                json={
                    "fileId": fileId,
                    "partSha1Array": hashes,
                },
                headers={"Authorization": self.__token},
            )
        except Exception as er:
            log.error("Error on finish large file")
            log.exception(er)

        if response.status_code != 200:
            logger.error(response.json())

        return response.json()

    async def get_media(self, media_id: int) -> Media:
        response = await self.client.get(f"{BASE_PATH}/{media_id}")
        return self.client.build_object(Media, response.data)

    async def update_media(
        self,
        media_id: int,
        media: Optional[Media] = None
    ) -> Media:
        """Update media"""
        media.id = media_id
        data = media.to_update_request()

        response = await self.client.put(
                BASE_PATH,
                data=data,
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
