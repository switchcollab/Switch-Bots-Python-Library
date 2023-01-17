from switch.base import SwitchObject
from typing import List

from .message import Message
from switch.api.common.models.user import User


class GroupChatHistory(SwitchObject):
    def __init__(
        self,
        users: List[User] = None,
        messages: List[Message] = None,
    ):
        self.users = users or []
        self.messages = messages or []

    def from_json(self, data: dict) -> "GroupChatHistory":
        self.users = User.build_from_json_list(data.get("users", []))
        self.messages = Message.build_from_json_list(data.get("messages", []))
        return self

    def to_json(self) -> dict:
        return {
            "users": [user.to_json() for user in self.users],
            "messages": [message.to_json() for message in self.messages],
        }