from typing import Optional
from swibots.base import SwitchObject
from swibots.utils.types import JSONDict


class BotCommand(SwitchObject):
    def __init__(
        self,
        command: Optional[str] = None,
        description: Optional[str] = None,
        channel: Optional[bool] = False,
    ):
        self.active = None
        self.bot_id = None
        self.command = command
        self.description = description
        self.channel = channel

    def from_json(self, data: JSONDict) -> "BotCommand":
        if data is not None:
            self.bot_id = data.get("botId")
            self.command = data.get("command")
            self.description = data.get("description") or data.get("commandDescription")
            self.channel = data.get("channel")
            self.active = data.get("active")
        return self

    def to_json(self) -> JSONDict:
        return {
            "botId": self.bot_id,
            "command": self.command,
            "description": self.description,
            "channel": self.channel,
        }
