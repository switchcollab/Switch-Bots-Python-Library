from .types import InlineQueryResultType
import swibots
from swibots.utils.types import JSONDict
from swibots.base import SwitchObject


class InputMessageContent(SwitchObject):
    def __init__(
            self,
            message_text: str = None,
    ):
        self.message_text = message_text

    def to_json(self) -> JSONDict:
        return {
            "messageText": self.message_text,
        }

    def from_json(self, data: JSONDict) -> "InputMessageContent":
        if data is not None:
            self.message_text = data.get("messageText")
        return self
