import swibots
from typing import Optional, List, Dict
from swibots.base import SwitchObject
from swibots.utils.types import JSONDict


class BotCommand(SwitchObject):
    def __init__(
        self,
        command: Optional[str] = None,
        description: Optional[str] = None,
        channel: Optional[bool] = False,
        subcommands: Optional[List["BotSubCommand"]] = None,
    ):
        self.active = None
        self.bot_id = None
        self.command = command
        self.description = description
        self.channel = channel
        self.subcommands = subcommands

    def from_json(self, data: JSONDict) -> "BotCommand":
        if data is not None:
            self.bot_id = data.get("botId")
            self.command = data.get("command")
            self.description = data.get("description") or data.get("commandDescription")
            self.channel = data.get("channel")
            self.active = data.get("active")
            self.subcommands = []

            for subcommand, value in data.get("subCommands", {}).items():
                self.subcommands.append(
                    BotSubCommand(
                        command=subcommand, options=value[0] if value else None
                    )
                )
        return self

    def to_json(self) -> JSONDict:
        subcommands = {}
        for command in self.subcommands or []:
            opts = [command.options] if command.options else []
            subcommands[command.command] = opts
        return {
            "botId": self.bot_id,
            "command": self.command,
            "description": self.description,
            "channel": self.channel,
            "subCommands": subcommands,
        }


class BotSubCommand(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        command: Optional[str] = None,
        options: Dict = None,
        **kwargs
    ):
        super().__init__(app, **kwargs)
        self.command = command
        self.options = options

    def to_json(self) -> JSONDict:
        return {self.command: [self.options] if self.options else None}
