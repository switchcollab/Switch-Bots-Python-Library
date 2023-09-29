from io import BytesIO
from swibots.base import SwitchObject
from swibots.utils.types import JSONDict
from ....api.common.models import Media
from typing import List, Optional, Union

import swibots


class Sticker(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        emoji: Optional[str] = None,
        sticker_pack_id: Optional[str] = None,
        created_by: Optional[int] = None,
        media_id: Optional[int] = None,
        sticker_info: Optional[Media] = None,
    ):
        super().__init__(app)
        self.id = id
        self.name = name
        self.description = description
        self.emoji = emoji
        self.sticker_pack_id = sticker_pack_id
        self.sticker_info = sticker_info
        self.created_by = created_by
        self.media_id = media_id

    def from_json(self, data: dict = None) -> "Sticker":
        if data is not None:
            self.id = data.get("id")
            self.name = data.get("name")
            self.description = data.get("description")
            self.emoji = data.get("linkedEmoji")
            self.sticker_info = Media.build_from_json(
                data.get("stickerMediaInfo", self.sticker_info)
            )
            self.sticker_pack_id = data.get("stickerPackId")
            self.created_by = int(data.get("createdBy", 0))
            self.media_id = data.get("stickerMediaId")
        return self

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "linkedEmoji": self.emoji,
            "stickerPackId": self.sticker_pack_id,
            "createdBy": self.created_by,
            "stickerMediaId": self.media_id,
            "stickerMediaInfo": self.sticker_info.to_json()
            if self.sticker_info
            else None,
        }

    async def delete(self) -> bool:
        return await self.app.delete_sticker(self.id)


class StickerPack(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        pack_type: Optional[str] = None,
        created_by: Optional[int] = None,
        access_control: Optional[str] = None,
        thumb_media_id: Optional[int] = None,
        thumb_info: Optional[Media] = None,
    ):
        super().__init__(app)
        self.id = id
        self.name = name
        self.created_by = created_by
        self.thumb_media_id = thumb_media_id
        self.thumb_info = thumb_info
        self.access_control = access_control
        self.pack_type = pack_type
        self.stickers: List[Sticker] = None

    def from_json(self, data: JSONDict | None) -> "StickerPack":
        if data is not None:
            self.id = data.get("id")
            self.name = data.get("name")
            self.created_by = int(data.get("createdBy", 0))
            self.pack_type = data.get("packType")
            self.thumb_media_id = data.get("thumbnailMediaId")
            self.thumb_info = Media.build_from_json(
                data.get("thumbnailMediaInfo"), self.app
            )
            self.stickers = data.get("sortedStickers")
        return self

    def to_json_request(self) -> JSONDict:
        return {
            "name": self.name,
            "id": self.id,
            "accessControl": self.access_control,
            "sortedStickers": self.stickers,
            "packType": self.pack_type,
        }

    async def delete(self) -> bool:
        return await self.app.delete_sticker_pack(self.id)

    async def add(
        self, sticker: str | BytesIO, name: str, description: str, emoji: str
    ) -> Sticker:
        return await self.app.create_sticker(
            sticker, name, description, emoji, pack_id=self.id
        )
