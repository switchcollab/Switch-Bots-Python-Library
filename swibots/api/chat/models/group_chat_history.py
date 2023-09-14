from swibots.base import SwitchObject
from typing import List

from .message import Message
from swibots.api.common.models.user import User
import swibots


class GroupChatHistory(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        users: List[User] = None,
        messages: List[Message] = None,
    ):
        super().__init__(app)
        self.users = users or []
        self.messages = messages or []

    def from_json(self, data: dict) -> "GroupChatHistory":
        self.users = User.build_from_json_list(data.get("userInfo", []), self.app)
        self.messages = Message.build_from_json_list(data.get("message", []), self.app)
        return self

    def to_json(self) -> dict:
        return {
            "userInfo": [user.to_json() for user in self.users],
            "message": [message.to_json() for message in self.messages],
        }
