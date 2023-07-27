from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject


class Media(SwitchObject):
    def __init__(
        self,
        id: Optional[int] = None,
        caption: Optional[str] = None,
        description: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        source_id: Optional[bool] = None,
        media_type: Optional[bool] = None,
        mime_type: Optional[str] = None,
        file_name: Optional[bool] = None,
        file_size: Optional[bool] = None,
        url: Optional[bool] = None,
    ):
        self.id = id
        self.caption = caption
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.source_id = source_id
        self.media_type = media_type
        self.mime_type = mime_type
        self.file_name = file_name
        self.file_size = file_size
        self.url = url

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "caption": self.caption,
            "description": self.description,
            "thumbnailUrl": self.thumbnail_url,
            "sourceId": self.source_id,
            "mediaType": self.media_type,
            "mimeType": self.mime_type,
            "fileName": self.file_name,
            "fileSize": self.file_size,
            "downloadUrl": self.url,
        }

    def from_json(self, data: Optional[JSONDict] = None) -> "Media":
        if data is not None:
            self.id = data.get("id")
            self.caption = data.get("caption")
            self.description = data.get("description")
            self.thumbnail_url = data.get("thumbnailUrl")
            self.source_id = data.get("sourceId")
            self.media_type = data.get("mediaType")
            self.mime_type = data.get("mimeType")
            self.file_name = data.get("fileName")
            self.file_size = data.get("fileSize")
            self.url = data.get("downloadUrl")
        return self
