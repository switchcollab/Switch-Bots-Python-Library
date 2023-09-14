from .types import InlineQueryResultType
import swibots
from swibots.utils.types import JSONDict
from swibots.base import SwitchObject
from .input_message_content import InputMessageContent
from ..inline_markup import InlineMarkup
from .inline_query_result import InlineQueryResult


class BaseTypedInlineQueryResult(InlineQueryResult):
    def __init__(
        self,
        id: str,
        type: InlineQueryResultType,
        title: str = None,
        description: str = None,
        thumb_url: str = None,
        thumb_width: int = None,
        thumb_height: int = None,
        input_message: "InputMessageContent" = None,
        reply_markup: "InlineMarkup" = None,
    ):
        super().__init__(id, type, input_message, reply_markup)
        self.type = type
        self.title = title
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    def to_json(self) -> JSONDict:
        data = super().to_json()
        data.update(
            {
                "title": self.title,
                "description": self.description,
                "thumbUrl": self.thumb_url,
                "thumbWidth": self.thumb_width,
                "thumbHeight": self.thumb_height,
            }
        )
        return data
