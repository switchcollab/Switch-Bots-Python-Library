from typing import Optional, List
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
from .embed_inline_field import EmbedInlineField
from .media_upload_request import MediaUploadRequest


class EmbeddedMedia(SwitchObject):
    def __init__(
        self,
        thumbnail: MediaUploadRequest | str,
        description: Optional[str] = None,
        footer_icon: Optional[str] = None,
        footer_title: Optional[str] = None,
        header_icon: Optional[str] = None,
        header_name: Optional[str] = None,
        inline_fields: Optional[List[List["EmbedInlineField"]]] = None,
        title: Optional[str] = None,
    ):
        super().__init__()
        self.thumbnail = thumbnail
        self.description = description
        self.footer_icon = footer_icon
        self.footer_title = footer_title
        self.header_icon = header_icon
        self.header_name = header_name
        self.inline_fields = inline_fields
        self.title = title

    def data_to_request(self):
        form_data = {
            "isEmbedMessage": "true",
            "embedMessage.title": self.title,
            "embedMessage.description": self.description,
            "embedMessage.headerName": self.header_name,
            "embedMessage.headerIcon": self.header_icon,
            "embedMessage.footerTitle": self.footer_title,
            "embedMessage.footerIcon": self.footer_icon,
        }
        for i, kb in enumerate(self.inline_fields or []):
            for j, b in enumerate(kb):
                key = "embedMessage.inlineFields[{0}][{1}].key".format(i, j)
                form_data[key] = b.key
                title_key = "embedMessage.inlineFields[{0}][{1}].title".format(i, j)
                form_data[title_key] = b.title
                icon_key = "embedMessage.inlineFields[{0}][{1}].icon".format(i, j)
                form_data[icon_key] = b.icon
        return form_data

    def from_json(self, data: JSONDict | None) -> "EmbeddedMedia":
        if data is not None:
            self.thumbnail = data.get("coverPic")
            self.description = data.get("description")
            self.footer_icon = data.get("footerIcon")
            self.footer_title = data.get("footerTitle")
            self.header_icon = data.get("headerIcon")
            self.header_name = data.get("headerName")
            self.title = data.get("title")
            self.inline_fields = [
                [
                    EmbedInlineField(
                        key=x.get("key"), icon=x.get("icon"), title=x.get("title")
                    )
                    for x in row
                ]
                for row in data.get("inlineFields", [])
            ]
        return self

    def to_json(self) -> JSONDict:
        return {
            "coverPic": self.thumbnail,
            "description": self.description,
            "footerIcon": self.footer_icon,
            "footerTitle": self.footer_title,
            "headerIcon": self.header_icon,
            "headerName": self.header_name,
            "inlineFields": [
                [x.to_json() for x in row] for row in (self.inline_fields or [])
            ],
            "title": self.title,
        }
