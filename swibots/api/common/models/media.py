import swibots
from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject


class Media(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[int] = None,
        caption: Optional[str] = None,
        checksum: Optional[str] = None,
        description: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        type_name: Optional[str] = None,
        source_id: Optional[bool] = None,
        media_type: Optional[int] = None,
        mime_type: Optional[str] = 0,
        file_name: Optional[bool] = None,
        file_size: Optional[bool] = None,
        url: Optional[bool] = None,
        owner_id: Optional[int] = None,
        owner_type: Optional[str] = None
    ):
        super().__init__(app)
        self.id = id
        self.caption = caption
        self.description = description
        self.checksum = checksum
        self.thumbnail_url = thumbnail_url
        self.source_id = source_id
        self.type_name = type_name
        self.media_type = media_type
        self.mime_type = mime_type
        self.file_name = file_name
        self.file_size = file_size
        self.owner_id = owner_id
        self.url = url
        self.owner_type = owner_type

    @property
    def is_sticker(self) -> bool:
        return 200 <= (self.media_type) <= 202

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "caption": self.caption,
            "checksum": self.checksum,
            "description": self.description,
            "thumbnailUrl": self.thumbnail_url,
            "sourceId": self.source_id,
            "mediaType": self.media_type,
            "mimeType": self.mime_type,
            "fileName": self.file_name,
            "fileSize": self.file_size,
            "typeName": self.type_name,
            "ownerId": self.owner_id,
            "ownerType": self.owner_type,
            "downloadUrl": self.url,
        }

    def from_json(self, data: Optional[JSONDict] = None) -> "Media":
        if data is not None:
            self.id = data.get("id")
            self.checksum = data.get("checksum")
            self.caption = data.get("caption")
            self.description = data.get("description")
            self.thumbnail_url = data.get("thumbnailUrl")
            self.source_id = data.get("sourceId")
            self.media_type = data.get("mediaType")
            self.mime_type = data.get("mimeType")
            self.file_name = data.get("fileName")
            self.file_size = data.get("fileSize")
            self.url = data.get("downloadUrl")
            self.owner_id = data.get("ownerId")
            self.owner_type = data.get("ownerType")
            if isinstance(self.owner_id, str) and self.owner_id.isdigit():
                self.owner_id = int(self.owner_id)

        return self

    async def edit(
        self, caption: Optional[str] = None, description: Optional[str] = None
    ):
        """Update media Info

        Args:
          caption: Caption of media
          description: Description to update.
        """
        return await self.app.update_media_info(
            self.id, caption=caption, description=description
        )
