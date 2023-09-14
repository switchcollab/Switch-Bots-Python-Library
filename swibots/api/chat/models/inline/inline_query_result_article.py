import swibots
from swibots.utils.types import JSONDict
from swibots.base import SwitchObject

from .base_typed_inline_query_result import BaseTypedInlineQueryResult
from .input_message_content import InputMessageContent
from ..inline_markup import InlineMarkup
from .types import InlineQueryResultType


class InlineQueryResultArticle(BaseTypedInlineQueryResult):
    def __init__(
        self,
        id: str,
        title: str,
        article_url: str,
        input_message: "InputMessageContent" = None,
        description: str = None,
        thumb_url: str = None,
        thumb_width: int = None,
        thumb_height: int = None,
        reply_markup: "InlineMarkup" = None,
    ):
        super().__init__(
            id,
            InlineQueryResultType.ARTICLE,
            title,
            description,
            thumb_url,
            thumb_width,
            thumb_height,
            input_message,
            reply_markup,
        )
        self.article_url = article_url

    def to_json(self) -> JSONDict:
        data = super().to_json()
        data.update(
            {
                "articleUrl": self.article_url,
            }
        )
        return data
