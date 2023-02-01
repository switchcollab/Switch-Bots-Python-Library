import asyncio
import os
import swibots

from swibots.utils.types import DownloadProgressCallback
from swibots.error import SwitchError
from swibots.api.chat.models import Message
from typing import Union, Optional, Callable, BinaryIO

DOWNLOAD_MEDIA = "downloads/"


class DownloadMedia:
    async def download_media(self: "swibots.ApiClient", message: Message, file_name: str = DOWNLOAD_MEDIA, in_memory: bool = False, block: bool = True, progress: DownloadProgressCallback = None, progress_args: tuple = ()) -> Optional[Union[BinaryIO, bytes]]:
        """
        """

        # 1 = IMAGE, 2 = VIDEO, 3 = AUDIO, 7 = FILE
        if message.status not in [1, 2, 3, 7]:
            raise SwitchError("Message is not a media message")

        if message.media_link is None:
            raise SwitchError("Message does not have a media link")

        media_file_name = message.media_link.split("/")[-1]
        directory, file_name = os.path.split(file_name or "")
        file_name = file_name or media_file_name or ""

        download_fn = self.handle_download(
            url=message.media_link, directory=directory, file_name=file_name, in_memory=in_memory, block=block, progress=progress, progress_args=progress_args)
        if block:
            return await download_fn
        else:
            asyncio.get_event_loop().create_task(download_fn)
