import logging, mimetypes
from swibots.utils import ReadCallbackStream
from typing import TYPE_CHECKING, List, Optional
from urllib.parse import urlencode
from ..models import Sticker, StickerPack
from io import BytesIO

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/sticker"


class StickerController:
    """Stickers controller"""

    def __init__(self, client: "ChatClient"):
        self.client = client

    async def get_stickers(
        self, pack_id: str, limit: int = 30, offset: int = 0
    ) -> List[Sticker]:
        data = {"stickerPackId": pack_id, "offset": offset, "limit": limit}
        response = await self.client.get(f"{BASE_PATH}?{urlencode(data)}")
        return self.client.build_list(Sticker, response.data)

    async def create_sticker(
        self,
        sticker: str | BytesIO,
        name: str,
        description: str,
        emoji: str,
        pack_id: str,
    ) -> Sticker:
        file_name = sticker.name if isinstance(sticker, BytesIO) else sticker
        response = await self.client.post(
            BASE_PATH,
            form_data={
                "stickerPackId": pack_id,
                "linkedEmoji": emoji,
                "name": name,
                "description": description,
            },
            files={
                "uploadMediaRequest.file": (
                    file_name,
                    ReadCallbackStream(sticker),
                    mimetypes.guess_type(file_name)[0],
                )
            },
        )
        return self.client.build_object(Sticker, response.data)

    async def delete_sticker(self, sticker_id: int) -> bool:
        await self.client.delete(f"{BASE_PATH}?id={sticker_id}")
        return True

    # region

    async def create_sticker_pack(
        self, name: str, pack_type: str, access: str, thumb: str | BytesIO
    ) -> StickerPack:
        form_data = {
            "name": name,
            "packType": pack_type,
            "accessControl": access,
        }
        files = None
        if thumb:
            thumb_name = thumb.name if isinstance(thumb, BytesIO) else thumb
            files = {
                "uploadMediaRequest.file": (
                    thumb_name,
                    ReadCallbackStream(thumb),
                    mimetypes.guess_type(thumb_name)[0],
                )
            }
        response = await self.client.post(
            f"{BASE_PATH}/pack", form_data=form_data, files=files
        )
        return self.client.build_object(StickerPack, response.data)

    async def delete_sticker_pack(self, pack_id: int) -> bool:
        await self.client.delete(f"{BASE_PATH}/pack?id={pack_id}")
        return True

    async def search_sticker_packs(
        self, query: str, limit: int = 30, offset: int = 0
    ) -> List[StickerPack]:
        data = {"query": query, "offset": offset, "limit": limit}
        response = await self.client.get(f"{BASE_PATH}/pack/search?{urlencode(data)}")
        return self.client.build_list(StickerPack, response.data)

    async def get_all_sticker_packs(self, limit: int = 10, offset: int = 0):
        data = {"limit": limit, "offset": offset}
        response = await self.client.get(f"{BASE_PATH}/pack?{urlencode(data)}")
        return self.client.build_list(StickerPack, response.data)

    async def sort_stickers(
        self, pack: StickerPack, sorted_stickers: List[str] = None
    ) -> StickerPack:
        pack.stickers = sorted_stickers
        response = await self.client.post(
            f"{BASE_PATH}/pack/sort",
            data=pack.to_json_request(),
        )
        return self.client.build_object(StickerPack, response.data)

    # endregion
