import swibots
from swibots.utils.types import JSONDict
from swibots.base import SwitchObject

from .base_typed_inline_query_result import BaseTypedInlineQueryResult
from .input_message_content import InputMessageContent
from ..inline_markup import InlineMarkup
from .types import InlineQueryResultType


class InlineQueryResultDocument(BaseTypedInlineQueryResult):
    def __init__(
        self,
        id: str,
        title: str,
        document_url: str,
        mime_type: str,
        input_message: "InputMessageContent" = None,
        description: str = None,
        thumb_url: str = None,
        thumb_width: int = None,
        thumb_height: int = None,
        reply_markup: "InlineMarkup" = None,
    ):
        super().__init__(
            id,
            InlineQueryResultType.DOCUMENT,
            title,
            description,
            thumb_url,
            thumb_width,
            thumb_height,
            input_message,
            reply_markup,
        )
        self.document_url = document_url
        self.mime_type = mime_type

    def to_json(self) -> JSONDict:
        data = super().to_json()
        data.update(
            {
                "documentUrl": self.document_url,
                "mimeType": self.mime_type,
            }
        )
        return data
