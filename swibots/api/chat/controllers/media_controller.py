import asyncio
import aiofiles
import base64
import hashlib
import httpx
import json
import logging
import mimetypes
import os
import random
import re
import tempfile
import uuid
from urllib.parse import urlparse
from datetime import datetime
from httpx import AsyncClient
from io import BytesIO
from typing import TYPE_CHECKING, Optional, Union
from typing import TYPE_CHECKING, Optional
from swibots.api.common.models import Media
from swibots.config import APP_CONFIG
from swibots.errors import UnknownBackBlazeError, FileTooLarge
from swibots.types import MAX_FILE_SIZE

from swibots.utils.types import (
    DownloadProgressCallback,
    IOClient,
    UploadProgress,
    UploadProgressCallback,
)

from swibots.errors import UnknownBackBlazeError, FileTooLarge
from swibots.utils.types import (
    UploadProgressCallback,
    DownloadProgressCallback,
    IOClient,
    UploadProgress,
)
from swibots.types import MAX_FILE_SIZE
from swibots.config import APP_CONFIG
from swibots.api.common.models import Media

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logger = logging.getLogger(__name__)

BASE_PATH = "/v1/media"

account_id = APP_CONFIG["BACKBLAZE"].get("ACCOUNT_ID")
application_key = APP_CONFIG["BACKBLAZE"].get("APPLICATION_KEY")

bucket_id = APP_CONFIG["BACKBLAZE"].get("BUCKET_ID")

headers = {}
headers["Authorization"] = (
    "Basic " + base64.b64encode(f"{account_id}:{application_key}".encode()).decode()
)
headers["accept"] = "application/json"

MAX_THUMB_SIZE = 1024 * 40
logging.getLogger("httpx").setLevel(logging.ERROR)


class ReadableFile:
    def __init__(self, file, name,
                 start_bytes: int = 0,
                 max_read: int = None):
        self.file = file
        self.name = name
        self.readed = 0
        self.file.seek(start_bytes)
        self.max_read_size = max_read

    def read(self, n):
        if self.max_read_size and self.readed > self.max_read_size:
            return b''

        chunk = self.file.read(n)
        self.readed += len(chunk)
        if self.max_read_size and self.readed > self.max_read_size:
            chunk = chunk[:self.max_read_size - self.readed]
        return chunk
    
    def close(self):
        if hasattr(self.file, 'close'):
            self.file.close()


class MediaService:
    def __init__(self) -> None:
        pass


    async def get_thumb_url(
        self, path: Union[str, BytesIO], for_document: bool = False, *args, **kwargs
    ) -> str:
        if not path:
            return

        if path and isinstance(path, str):
            # check for valid urls
            parse = urlparse(path)
            if parse.scheme and parse.netloc:
                return path

        __remove = False
        mime_type = (
            mimetypes.guess_type(path.name if isinstance(path, BytesIO) else path)[0]
            or "application/octet-stream"
        )
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
            size = path.getbuffer().nbytes
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
                log.warning(
                    "[Pillow is not installed] and [thumb size is greater than 20kb], ignoring thumb"
                )
                return

        _, ext = os.path.splitext(name)
        file_name = f"{uuid.uuid1()}{ext}"

        output = await self.file_to_response(
            path, mime_type, file_name, content=content, remove=__remove
        )
        if isinstance(output, dict):
            return output['downloadUrl']

        path, file = output
        return f"{self.url}/file/{self.bucket_name}/{file['fileName']}"


    async def generate_from_ffmpeg(self, path: str, hw: int):
        log.debug("checking for ffmpeg")
        ffmpeg_path = os.getenv("FFMPEG_PATH") or "ffmpeg"
        try:
            proc = await asyncio.create_subprocess_exec(
                ffmpeg_path, stderr=asyncio.subprocess.PIPE
            )
            await proc.wait()
        except Exception as er:
            logger.error(er)
            return
        if b"ffmpeg version" not in (er := await proc.stderr.read()):
            log.info(f"ffmpeg is not installed, {er}")
            return
        name = os.path.join(tempfile.gettempdir(), f"{uuid.uuid1()}.png")
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


class StorageMediaService(MediaService):
    def __init__(self, client: "ChatClient") -> None:
        self.client = client
        self.api_url = "https://storage.switch.click"

        self._min_file_size = 100 * 1024 * 1024
    
    async def get_upload_url(self):
        async with AsyncClient(timeout=None) as client:
            response = await client.get(f"{self.api_url}/get_upload_url")
            return response.json()['url']


    async def check_if_active(self):
        try:
            async with AsyncClient(timeout=None) as client:
                resp = await client.get(self.api_url)
                assert resp.status_code == 200
                return True
        except Exception as e:
            log.error(f"Failed to check if api is active: {e}")
            return False

    async def start_large_file(self,  file_name: str, file_size: int):
        logger.info(f"Starting large file upload for {file_name} with size {file_size}")

        upload_url = await self.get_upload_url()    
        async with AsyncClient(timeout=None) as client:
            response = await client.post(f"{upload_url}/start_large_file",
                                         json={
                "file_name": os.path.basename(file_name),
                "file_size": file_size
            })
        response_data = response.json()
        response_data['upload_url'] = upload_url
        return response_data


    async def upload_part(self, upload_url: str, path: str, fileId: str, start_bytes: int, part_size: int, part_number: int,
                          progress: UploadProgress):
        if isinstance(path, str):
            path = open(path, "rb")

        file = ReadableFile(path, path,
                           start_bytes=start_bytes,
                           max_read=part_size)

        async def __upload_part():
            async with AsyncClient(timeout=None) as client:
                response = await client.post(
                    "{}/upload_part?fileId={}&partNumber={}".format( 
                        upload_url, fileId, part_number
                    ),
                        files={
                            "file": file,
                        },
                )
                print(response.text)
            return response.json()
        
        try:
            task = asyncio.create_task(__upload_part())

            readed = 0
            if progress.callback:
                while not task.done():
                    await asyncio.sleep(0.1)
                    if readed != file.readed:
                        change_read = file.readed - readed
                        if change_read + progress.readed <= progress.total:
                            await progress.bytes_readed(change_read)
                        readed = file.readed
            else:
                await task
        finally:
            file.close()

        return task.result()



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
        part_size: int = int(os.getenv("UPLOAD_PART_SIZE", 100 * 1024 * 1024)),
        task_count: int = int(os.getenv("UPLOAD_TASKS", 0)),
        for_document: bool = False,
        premium: bool = False,
        retries: int = 10,

    ) -> Media:
        _is_bytesio = isinstance(path, BytesIO)
        if not  part_size or part_size < self._min_file_size:
            part_size = self._min_file_size

        if not _is_bytesio:
            size = os.path.getsize(path)
        else:
            size = path.getbuffer().nbytes

        if size > MAX_FILE_SIZE:
            raise FileTooLarge(f"{path}: file size is too big to upload!")

        if not mime_type:
            mime_type = (
                    mimetypes.guess_type(path.name if isinstance(path, BytesIO) else path)[0]
                    or "application/octet-stream"
            )
        
        if size <= self._min_file_size:
            response = await self.file_to_response(
                path=path,
                callback=callback,
                callback_args=callback_args,
                file_size=size,
                mime_type=mime_type
            )
            downloadUrl = response['downloadUrl']
        else:
            if not file_name:
                file_name = os.path.basename(path)

            response = await self.start_large_file(file_name, size)
            upload_url = response['upload_url']

            queue = asyncio.Queue()
            progress = UploadProgress(
            path=path,
            callback=callback,
            callback_args=callback_args,
            client=IOClient(),
            size=size,
        )
            upl_size = 0
            part_number = 0
            while upl_size < size:
                await queue.put(
                    self.upload_part(
                        path=path,
                        upload_url=upload_url,
                        start_bytes=upl_size,
                        part_size= part_size,
                        fileId=response['fileId'],
                        part_number=part_number,
                        progress=progress
                    )
                )
                upl_size += part_size
                part_number += 1

            logger.info(f"total parts: {part_number - 1}")

            async def runFromQueue():
                while not queue.empty():
                    try:
                        task = await queue.get()
                        await task
                    except Exception as er:
                        log.exception(er)

            qTask = [asyncio.create_task(runFromQueue()) for _ in range(task_count)]

            try:
                await asyncio.wait(qTask)
            except Exception as er:
                log.exception(er)

            for q in qTask:
                if q.done() and (exc := q.exception()):
                    log.exception(exc)
                if not q.done():
                    q.cancel()

            response = await self.complete_large_file(upload_url, response['fileId'], part_number)
            downloadUrl = response['downloadUrl']

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
            "fileSize": size,
            "fileName": file_name or os.path.basename(path),
            "downloadUrl": downloadUrl,
            "thumbnailUrl": thumbUrl,
            "mediaType": media_type,
            "sourceUri": response['fileId'],
            "checksum": ' ',
            "ownerId": self.client.app.user.id,
            "premium": premium,
        }

        return self.client.build_object(Media, media)

    async def complete_large_file(self, upload_url: str, file_id: str, total_parts: int):
        async with AsyncClient(timeout=None) as client:
            response = await client.post(f"{upload_url}/finish_large_file",
                                         json={
                                             "totalParts": total_parts,
                                             "fileId": file_id,
                                             "blocking": True
                                         })
            return response.json()


    async def file_to_response(self,
        path: str | BytesIO,
        mime_type=None,
        file_name=None,
        content: bytes = None,
        callback=None,
        callback_args=None,
        file_size=None,
        remove: bool = None,
    ):
        upload_url = await self.get_upload_url()
        Isbytes = isinstance(path, BytesIO)

        if not Isbytes:
            file = open(path, "rb")
        file = ReadableFile(file, path.name if Isbytes else path)

        if not mime_type:
            mime_type = (
                mimetypes.guess_type(path.name if Isbytes else path)[0]
                or "application/octet-stream"
            )

        async def upload_file():
            async with AsyncClient(timeout=None) as client:
                response = await client.post(
                        f"{upload_url}/upload?blocking=true",
                        files={"file": file}
                    )
                jsonData = response.json()

            file.close()
            return jsonData
        
        task = asyncio.create_task(upload_file())

        if callback:
                readed = 0
                while not task.done():
                    await asyncio.sleep(0.1)
                    if readed != file.readed:
                        readed = file.readed
                        progress = UploadProgress(
                            path=path,
                            callback=callback,
                            callback_args=callback_args,
                            client=IOClient(),
                            size=file_size,
                        )
                        await progress.bytes_readed(file.readed)
        else:
                await task
   
        result = task.result()
        if remove and not Isbytes:
            os.remove(path)

        return result



class MediaController(MediaService):
    """Media controller
    This controller is used to communicate with the media endpoints.
    """

    MIN_WAIT = 3
    MAX_WAIT = 7

    def __init__(self, client: "ChatClient", bucket_name: str = "ssbucket"):
        self.client = client
        self.__token = None
        self.url = None
        self._min_part_size = 5000000
        self.bucket_name = bucket_name
        self.storage_service = StorageMediaService(client)


    async def getAccountInfo(self):
        response = await self.request(
            "https://api.backblazeb2.com/b2api/v2/b2_authorize_account",
            headers=headers,
            method="GET",
        )
        data = response.json()
        self.url = data['apiUrl']

        if token := data.get("authorizationToken"):
            self.__token = token
        log.debug(data)
        if min_size := data.get("absoluteMinimumPartSize"):
            self._min_part_size = min_size

        return self.__token


    async def file_to_response(
        self,
        path: str | BytesIO,
        mime_type=None,
        file_name=None,
        content: bytes = None,
        callback=None,
        callback_args=None,
        file_size=None,
        remove: bool = None,
    ):
        token = self.__token or await self.getAccountInfo()
        Isbytes = isinstance(path, BytesIO)

        if not mime_type:
            mime_type = (
                mimetypes.guess_type(path.name if Isbytes else path)[0]
                or "application/octet-stream"
            )

        head = {
            "Content-Type": "application/json",
            "Authorization": token,
        }
        rsp = await self.request(
            f"{self.url}/b2api/v2/b2_get_upload_url?bucketId={bucket_id}",
            method="GET",
            headers=head,
        )

        response_data = rsp.json()
        if not response_data.get("authorizationToken"):
            raise UnknownBackBlazeError(response_data)
        token = response_data["authorizationToken"]

        respp = rsp.json()
        if not respp.get("uploadUrl"):
            raise UnknownBackBlazeError(respp)

        with path if Isbytes else open(path, "rb") as f:
            content = f.read()
            file_sha1 = hashlib.sha1(content).hexdigest()

            headers = {
                "Authorization": token,
                "X-Bz-File-Name": file_name,
                "Content-Type": mime_type,
                "X-Bz-Content-Sha1": file_sha1,
                "Content-Length": str(len(content)),
            }

            rsp = await self.request(
                respp["uploadUrl"],
                headers=headers,
                data=content,
            )
            if Isbytes:
                path = BytesIO(content)
                path.name = file_name
        if remove:
            os.remove(path)

        file_response = rsp.json()
        if "contentLength" in file_response:
            if callback:
                progress = UploadProgress(
                    path=path,
                    callback=callback,
                    callback_args=callback_args,
                    client=IOClient(),
                    size=file_size,
                )
                await progress.bytes_readed(file_response["contentLength"])
        else:
            log.error(file_response)
        return path, file_response


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
        premium: bool = False,
        retries: int = 10,
        private_community: bool = False,
        storage_method_retries: int = 3

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
        if not task_count:
            task_count = 1

        if not file_name:
            if isinstance(path, BytesIO):
                file_name = path.name
            else:
                file_name = path

        if private_community or self.client.app._upload_mode == "STORAGE":
            if await self.storage_service.check_if_active():
                for _ in range(storage_method_retries):
                    if _:
                        logger.info(f"Retrying storage method: {_}")
                    try:
                        return await self.storage_service.upload_media(
                            path=path,
                            caption=caption,
                            file_name=file_name,
                            description=description,
                            thumb=thumb,
                            mime_type=mime_type,
                            media_type=media_type,
                            callback=callback,
                            callback_args=callback_args,
                            auto_thumb=auto_thumb,
                            part_size=part_size,
                            task_count=task_count,
                            premium=premium,
                        retries=retries,
                        for_document=for_document,
                        )
                    except Exception as er:
                        logger.error(f"Error in storage method: {er}")
                        logger.exception(er)

        if not part_size:
            part_size = self._min_part_size

        if not min_file_size:
            min_file_size = self._min_part_size


        if part_size < self._min_part_size:
            log.warning(
                f"part_size cant be smaller than minimum [{self._min_part_size}]"
            )
            part_size = self._min_part_size


        if not mime_type:
            mime_type = mimetypes.guess_type(file_name)[0] or "application/octet-stream"
        log.debug(f"Sending request to backblaze: {path}")
        _is_bytesio = isinstance(path, BytesIO)

        if not _is_bytesio:
            size = os.path.getsize(path)
        else:
            size = path.getbuffer().nbytes
        if size > MAX_FILE_SIZE:
            raise FileTooLarge(f"{path}: file size is too big to upload!")
        _, ext = os.path.splitext(path.name if _is_bytesio else path)
        file_name = f"{uuid.uuid1()}{ext}"

        if (
            size > min_file_size
            and size > self._min_part_size
            and (size // part_size) > 1
        ):
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
                retries=retries,
            )
        else:
            path, file_response = await self.file_to_response(
                path,
                mime_type,
                file_name,
                callback=callback,
                file_size=size,
                callback_args=callback_args,
            )
        if not file_response.get("fileName"):
            raise UnknownBackBlazeError(file_response)
        url = f"{self.url}/file/{self.bucket_name}/{file_response['fileName']}"
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
            "premium": premium,
        }
        return self.client.build_object(Media, media)

    async def request(self, url: str, method: str = "POST", **kwargs):
        async with AsyncClient(
            verify=False, timeout=None, headers=kwargs.get("headers")
        ) as client:
            resp = await (client.post if method == "POST" else client.get)(
                url, **kwargs
            )
            message = resp.json()
            if message.get("code") == "expired_auth_token":
                log.error("Expired auth token, retrying")
                token = await self.getAccountInfo()
                headers = kwargs.get("headers") or {}
                headers["Authorization"] = token
                kwargs["headers"] = headers
                return await self.request(url, method, **kwargs)
            elif message.get("code") == "service_unavailable":
                log.error(message)
                randomTime = random.randint(self.MIN_WAIT, self.MAX_WAIT)
                log.info(f"Waiting for {randomTime} before retry!")
                await asyncio.sleep(randomTime)
                return await self.request(url, method, **kwargs)
            return resp

    async def __upload_file(
        self,
        token,
        part_number,
        path,
        upl_size,
        part_size,
        fileId: str,
        progress: UploadProgress,
        retries: int = 10,
        wait_factor: int = 6,
    ):
        async with aiofiles.open(path, "rb") as f:
            for _ in range(retries):
                try:
                    respp = await self.request(
                        f"{self.url}/b2api/v2/b2_get_upload_part_url",
                        json={"fileId": fileId},
                        headers={"Authorization": token},
                        timeout=30,
                    )
                    break
                except Exception as er:
                    log.debug(er)
                    log.error(er)
                    if _ == (retries - 1):
                        raise er

            resp_data = respp.json()
            if respp.status_code != 200:
                logger.error("on Part url")
                logger.error(resp_data)
                raise UnknownBackBlazeError(resp_data)

            token = resp_data["authorizationToken"]
            upload_part_url = resp_data["uploadUrl"]

            await f.seek(upl_size)
            chunk = await f.read(part_size)

            for _ in range(retries + 1):
                if _:
                    log.info(f"Retrying upload [{path}][{upl_size}:{part_size}]")
                try:
                    respp = await self.request(
                        upload_part_url,
                        data=chunk,
                        headers={
                            "Authorization": token,
                            "X-Bz-Part-Number": str(part_number),
                            "X-Bz-Content-Sha1": hashlib.sha1(chunk).hexdigest(),
                        },
                    )
                    resp_data = respp.json()
                    if resp_data.get("code") == "service_unavailable":
                        log.error(resp_data)
                        log.info(f"Waiting for {_ * wait_factor}")
                        await asyncio.sleep(_ * wait_factor)
                        continue
                    if respp.status_code != 200:
                        logger.error("onUpload")
                        logger.error(resp_data)
                    hash = resp_data["contentSha1"]
                    await progress.bytes_readed(resp_data["contentLength"])
                    return hash, resp_data["partNumber"]
                except (httpx.WriteError, httpx.ReadError) as er:
                    log.exception(er)
                    log.error(er.request)
                except Exception as er:
                    log.exception(er)

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
        retries: int = None,
    ):
        log.info("getting account info")
        token = await self.getAccountInfo()

        progress = UploadProgress(
            path=path,
            callback=callback,
            callback_args=callback_args,
            client=IOClient(),
            size=file_size,
        )
        if isinstance(path, BytesIO) and not file_name:
            file_name = path.name
        upl_size = 0
        head = {
            "Content-Type": content_type,
            "X-Bz-File-Name": file_name,
            "Authorization": token,
        }
        data = {
            "fileName": file_name,
            "contentType": content_type,
            "bucketId": bucket_id,
            "fileInfo": file_info,
        }
        partHash = {}
        logger.info("start large file")
        respp = await self.request(
            f"{self.url}/b2api/v2/b2_start_large_file",
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
        queue = asyncio.Queue()

        async def runFromQueue():
            while queue.qsize():
                task = await queue.get()
                try:
                    hash, part_number = await task
                except Exception as er:
                    log.exception(er)
                    continue
                partHash[hash] = part_number

        try:
            while upl_size < file_size:
                await queue.put(
                    self.__upload_file(
                        token,
                        part_number,
                        path,
                        upl_size,
                        part_size,
                        fileId,
                        progress,
                        retries=retries
                    )
                )
                part_number += 1
                upl_size += part_size
        except Exception as er:
            log.exception(er)
        qTask = [asyncio.create_task(runFromQueue()) for _ in range(task_count)]

        try:
            await asyncio.wait(qTask)
        except Exception as er:
            log.exception(er)

        for q in qTask:
            if q.done() and (exc := q.exception()):
                log.exception(exc)
            if not q.done():
                q.cancel()

        if not partHash:
            raise Exception("parts are not found!")
        response = await self.__finish_large_file(
            partHash, fileId, path, part_size=part_size, progress=progress, token=token
        )
        return response

    async def __finish_large_file(
        self, partHash, fileId, path, part_size, progress, token, retry_count: int = 0
    ):
        if retry_count > 3:
            raise Exception("Max retries reached for finish file")
        hashes = list(map(lambda x: x[0], sorted(partHash.items(), key=lambda x: x[1])))
        try:
            response = await self.request(
                f"{self.url}/b2api/v2/b2_finish_large_file",
                json={
                    "fileId": fileId,
                    "partSha1Array": hashes,
                },
                headers={"Authorization": token},
            )
        except Exception as er:
            log.error("Error on finish large file")
            log.exception(er)
            log.info("canceling upload")
            resp = await self.request(
                f"{self.url}/b2api/v2/b2_cancel_large_file",
                data={"fileId": fileId},
                headers={"Authorization": token},
            )
            log.info(resp)
            log.info(resp.json())
        response = response.json()
        if response.get("code") == "bad_request":
            logger.info(response)
            mtch = re.search(
                "Part number (\d+) has not been uploaded", response.get("message")
            )
            if mtch:
                part_number = int(mtch.group(1))
                hash, part_number = await self.__upload_file(
                    token,
                    part_number,
                    path,
                    fileId=fileId,
                    upl_size=part_size * (part_number - 1),
                    part_size=part_size,
                    progress=progress,
                )
                partHash[hash] = part_number
                retry_count += 1
                return await self.__finish_large_file(
                    partHash,
                    fileId,
                    path,
                    part_size,
                    progress,
                    token=token,
                    retry_count=retry_count,
                )
        return response

    async def get_media(self, media_id: int) -> Media:
        response = await self.client.get(f"{BASE_PATH}/{media_id}")
        return self.client.build_object(Media, response.data)

    async def update_media(self, media_id: int, media: Optional[Media] = None) -> Media:
        data = media.to_update_request()

        data["id"] = media_id
        data = {x: y for x, y in data.items() if y}
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
