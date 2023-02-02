import swibots
from swibots.utils.types import JSONDict
from swibots.base import SwitchObject

from .base_typed_inline_query_result import BaseTypedInlineQueryResult
from .input_message_content import InputMessageContent
from ..inline_markup import InlineMarkup
from .types import InlineQueryResultType


class InlineQueryResultVideo(BaseTypedInlineQueryResult):
    def __init__(self,
                 id: str,
                 title: str,
                 video_url: str,
                 mime_type: str = None,
                 video_width: int = None,
                 video_height: int = None,
                 video_duration: int = None,
                 caption: str = None,
                 input_message: "InputMessageContent" = None,
                 description: str = None,
                 thumb_url: str = None,
                 thumb_width: int = None,
                 thumb_height: int = None,
                 reply_markup: "InlineMarkup" = None,
                 ):
        super().__init__(id, InlineQueryResultType.VIDEO, title, description, thumb_url, thumb_width, thumb_height,
                         input_message, reply_markup)
        self.video_url = video_url
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.caption = caption
        self.mime_type = mime_type

    def to_json(self) -> JSONDict:
        data = super().to_json()
        data.update({
            "videoUrl": self.video_url,
            "videoWidth": self.video_width,
            "videoHeight": self.video_height,
            "videoDuration": self.video_duration,
            "caption": self.caption,
            "mimeType": self.mime_type,
        })
        return data
