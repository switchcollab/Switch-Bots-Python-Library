import asyncio
import os
import json
import logging
from typing import TYPE_CHECKING, List, Optional

from swibots.api.chat.models import (
    Message,
    GroupChatHistory,
    InlineMarkup,
    InlineQuery,
    InlineQueryAnswer,
)
from swibots.api.common.models import User, MediaUploadRequest, Media, EmbeddedMedia
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

    async def upload_media(self, path: str | MediaUploadRequest) -> Media:
        """upload media from path or with MediaUploadRequest"""
        if isinstance(path, str):
            path = MediaUploadRequest(path)
        
        url = f"{BASE_PATH}/upload-multipart"
        files = path.file_to_request(url)
        form_data = path.data_to_params_request()
        files["file"] = files["uploadMediaRequest.file"]
        del files["uploadMediaRequest.file"]

        response = await self.client.post(BASE_PATH, form_data=form_data, files=files)
        files["file"][1].close()

        return self.client.build_object(Media, response.data)
