import swibots
from swibots.utils.types import JSONDict
from swibots.base import SwitchObject

from .base_typed_inline_query_result import BaseTypedInlineQueryResult
from .input_message_content import InputMessageContent
from ..inline_markup import InlineMarkup
from .types import InlineQueryResultType


class InlineQueryResultPhoto(BaseTypedInlineQueryResult):
    def __init__(self,
                 id: str,
                 title: str,
                 photo_url: str,
                 mime_type: str = None,
                 photo_width: int = None,
                 photo_height: int = None,
                 caption: str = None,
                 input_message: "InputMessageContent" = None,
                 description: str = None,
                 thumb_url: str = None,
                 thumb_width: int = None,
                 thumb_height: int = None,
                 reply_markup: "InlineMarkup" = None,
                 ):
        super().__init__(id, InlineQueryResultType.PHOTO, title, description, thumb_url, thumb_width, thumb_height,
                         input_message, reply_markup)
        self.photo_url = photo_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.caption = caption
        self.mime_type = mime_type

    def to_json(self) -> JSONDict:
        data = super().to_json()
        data.update({
            "photoUrl": self.photo_url,
            "photoWidth": self.photo_width,
            "photoHeight": self.photo_height,
            "caption": self.caption,
            "mimeType": self.mime_type,
        })
        return data
