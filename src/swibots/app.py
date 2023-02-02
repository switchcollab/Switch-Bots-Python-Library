import asyncio
from contextlib import AbstractContextManager
from io import BytesIO
import logging
import mimetypes
import os
import re
import shutil
import signal
from signal import signal as signal_fn, SIGINT, SIGTERM, SIGABRT
from typing import Callable, Optional
import swibots
from swibots.api import ApiClient
from swibots.api.auth.models import AuthUser
from swibots.error import CancelError, SwitchError
from swibots.utils import RestClient, DownloadProgressCallback, UploadProgress, DownloadProgress, IOClient, ReadCallbackStream
import httpx

log = logging.getLogger(__name__)

# Signal number to name
signals = {
    k: v for v, k in signal.__dict__.items() if v.startswith("SIG") and not v.startswith("SIG_")
}


class App(AbstractContextManager, ApiClient):
    def __init__(
        self,
        # username: Optional[str] = None,
        # password: Optional[str] = None,
        token: Optional[str] = None,
        loop: asyncio.AbstractEventLoop = None,
    ):
        """Initialize the client"""
        super().__init__()
        self.token = token
        self._loop = loop or asyncio.get_event_loop()
        self._running = False
        self._user_type = AuthUser
        self.on_community_service_start: Callable = None
        self.on_chat_service_start: Callable = None
        self.on_app_stop: Callable = None
        self.on_app_start: Callable = None
        self.rest_client = RestClient()

    async def handle_upload(self, url, file_name, data=None, file_field="file", progress=None,  progress_args: tuple = ()):
        dProgress = UploadProgress(
            current=0,
            readed=0,
            file_name=file_name,
            client=IOClient(),
            url=file_name,
            callback=progress,
            callback_args=progress_args
        )
        file = open(file_name, "rb")
        reader = ReadCallbackStream(
            file, dProgress.update
        )
        mime = mimetypes.guess_type(file_name)[0] or "application/octet-stream"
        try:
            r = await self.rest_client._client.post(url, files={file_field: (file_name, reader, mime)}, data=data, headers={"Authorization": f"Bearer {self.token}"})
            return r.json()
        except CancelError:
            pass

    async def handle_download(self, url: str, file_name: str, directory="downloads/", in_memory: bool = False, block: bool = True, progress: DownloadProgressCallback = None, progress_args: tuple = ()):
        if directory is None or directory == "":
            directory = "downloads/"
        os.makedirs(directory, exist_ok=True) if not in_memory else None
        temp_file_path = os.path.abspath(
            re.sub("\\\\", "/", os.path.join(directory, file_name))) + ".temp"
        file = BytesIO() if in_memory else open(temp_file_path, "wb")

        dProgress = DownloadProgress(
            total=0,
            downloaded=0,
            file_name=file_name,
            client=IOClient(),
            url=url,
        )

        if (progress):
            await progress(dProgress, *progress_args)

        try:
            with httpx.stream("GET", url) as response:
                dProgress.total = int(response.headers["Content-Length"])
                dProgress.downloaded = response.num_bytes_downloaded
                dProgress.client = response
                dProgress.started = True
                for chunk in response.iter_bytes():
                    file.write(chunk)
                    dProgress.downloaded += len(chunk)
                    if progress:
                        await progress(dProgress, *progress_args)

        except BaseException as e:
            if not in_memory:
                file.close()
                os.remove(temp_file_path)
            if isinstance(e, CancelError):
                return None
            if isinstance(e, asyncio.CancelledError):
                raise e

            return None
        else:
            if in_memory:
                file.name = file_name
                return file
            else:
                file.close()
                file_path = os.path.splitext(temp_file_path)[0]
                shutil.move(temp_file_path, file_path)
                return file_path

        # file_id, directory, file_name, in_memory, file_size, progress, progress_args = packet

        # os.makedirs(directory, exist_ok=True) if not in_memory else None
        # temp_file_path = os.path.abspath(re.sub("\\\\", "/", os.path.join(directory, file_name))) + ".temp"
        # file = BytesIO() if in_memory else open(temp_file_path, "wb")

        # try:
        #     async for chunk in self.get_file(file_id, file_size, 0, 0, progress, progress_args):
        #         file.write(chunk)
        # except BaseException as e:
        #     if not in_memory:
        #         file.close()
        #         os.remove(temp_file_path)

        #     if isinstance(e, asyncio.CancelledError):
        #         raise e

        #     return None
        # else:
        #     if in_memory:
        #         file.name = file_name
        #         return file
        #     else:
        #         file.close()
        #         file_path = os.path.splitext(temp_file_path)[0]
        #         shutil.move(temp_file_path, file_path)
        #         return file_path

    async def _validate_credentials(self):
        if self.token is not None:
            return await self._validate_token()
        if self.username is None or self.password is None:
            raise SwitchError(
                "Username and password are required when token is not set")
        user = await self.login(user_type=self._user_type)
        self.user = user

    async def _validate_token(self):
        # check if token is valid
        if self.token is None:
            raise SwitchError("Token is not set")

        try:
            log.debug("checking token...")
            user = await self.get_me(user_type=self._user_type)
            self.user = user
            log.info("Logged in as [%s][%d]", user.user_name, user.id)
        except Exception as e:
            log.exception(e)
            await self.stop()
            raise SwitchError("Invalid token")

        if self.user is None:
            raise SwitchError("Invalid token")

    async def _validate_run(self):
        await self._validate_credentials()

    async def _on_app_stop(self):
        await self.chat_service.stop()
        await self.community_service.stop()
        if self.on_app_stop is not None:
            await self.on_app_stop(self)

    async def _on_app_start(self):
        if self.on_app_start is not None:
            await self.on_app_start(self)

    async def start(self):
        try:
            if self._running:
                raise SwitchError("App is already running")
            self._running = True
            """Starts the app"""
            log.info("🚀 Starting app...")

            await self._validate_run()

            try:
                await (self.chat_service.start())
                if self.on_chat_service_start is not None:
                    await self.on_chat_service_start(self)
            except Exception as e:
                log.exception(e)

            try:
                await (self.community_service.start())
                if self.on_community_service_start is not None:
                    await self.on_community_service_start(self)
            except Exception as e:
                log.exception(e)

            await self._on_app_start()

            log.info("🚀 App started!")

            # # run forever
            # while self._running:
            #     await asyncio.sleep(1)
        except asyncio.CancelledError:
            self._running = False
            # await self._do_stop()

    async def _do_stop(self):
        log.info("🛑 Stopping app...")
        await self._on_app_stop()
        self._running = False

    async def stop(self):
        if not self._running:
            return
        await self._do_stop()

    def __enter__(self):
        return self.start()

    def __exit__(self, *args):
        try:
            self.stop()
        except ConnectionError:
            pass

    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self, *args):
        try:
            await self.stop()
        except ConnectionError:
            pass

    async def idle(self):
        task = None

        def signal_handler(signum, __):
            logging.info(
                f"Stop signal received ({signals[signum]}). Exiting...")
            task.cancel()

        for s in (SIGINT, SIGTERM, SIGABRT):
            signal_fn(s, signal_handler)

        while True:
            task = asyncio.create_task(asyncio.sleep(600))

            try:
                await task
            except asyncio.CancelledError:
                break

    def run(self, task: Callable = None):
        loop = asyncio.get_event_loop()
        run = loop.run_until_complete
        if task is not None:
            run(task)
        else:
            try:
                run(self.start())
                run(self.idle())
                run(self.stop())
            except KeyboardInterrupt:
                run(self.stop())
            except Exception as e:
                log.exception(e)
                run(self.stop())
