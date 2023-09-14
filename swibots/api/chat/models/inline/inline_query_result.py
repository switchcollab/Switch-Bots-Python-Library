from .types import InlineQueryResultType
import swibots
from swibots.base import SwitchObject
from swibots.utils.types import JSONDict
from .input_message_content import InputMessageContent
from ..inline_markup import InlineMarkup


class InlineQueryResult(SwitchObject):
    def __init__(
        self,
        id: str,
        type: InlineQueryResultType,
        input_message: "InputMessageContent" = None,
        reply_markup: "InlineMarkup" = None,
    ):
        self.id = id
        self.type = type
        self.input_message = input_message
        self.reply_markup = reply_markup

    def to_json(self) -> JSONDict:
        data = {
            "id": self.id,
            "type": self.type.value,
        }
        if self.input_message is not None:
            data["inputMessage"] = self.input_message.to_json()
        if self.reply_markup is not None:
            data["replyMarkup"] = self.reply_markup.to_json()
        return data
