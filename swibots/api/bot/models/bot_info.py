import json
from typing import TYPE_CHECKING, List, Optional
from swibots.api.common.models import User
from swibots.api.callback import AppPage
from swibots.utils.types import JSONDict
from swibots.base import SwitchObject
from .bot_command import BotCommand
from typing import Dict, Any


class BotWelcome(SwitchObject):
    def __init__(
        self,
        text: Optional[str] = None,
        button: Optional[str] = None,
        command: Optional[str] = None,
        thumb: Optional[str] = None,
    ):
        self.text = text
        self.thumb = thumb
        self.button = button
        self.command = command

    def to_json(self) -> JSONDict:
        return {
            "welcomeImage": self.thumb,
            "welcomeText": self.text,
            "buttonName": self.button,
            "buttonCommand": self.command,
        }

    def from_json(self, data: Dict[str, Any] | None) -> Any:
        if data:
            self.thumb = data.get("welcomeImage")
            self.text = data.get("welcomeText")
            self.button = data.get("buttonName")
            self.command = data.get("buttonCommand")
        return self


class BotInfo(User):
    def __init__(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        username: Optional[str] = None,
        image_url: Optional[str] = None,
        active: Optional[bool] = None,
        deleted: Optional[bool] = None,
        role_info: Optional[str] = None,
        admin: Optional[bool] = None,
        is_bot: Optional[bool] = None,
        commands: Optional[List[BotCommand]] = None,
        description: Optional[str] = None,
        welcome: BotWelcome = None,
        source_code: Optional[str] = None,
        preview: Optional[AppPage] = None,
    ):
        super().__init__(
            id=id,
            name=name,
            username=username,
            image_url=image_url,
            active=active,
            deleted=deleted,
            role_info=role_info,
            admin=admin,
            is_bot=is_bot,
        )
        self.commands: List[BotCommand] = commands or []
        self.description: Optional[str] = description
        self.source_code = source_code
        self.welcome = welcome
        self.preview = preview

    def to_json_request(self) -> JSONDict:
        data = {
            "commands": [command.to_json() for command in self.commands],
            "description": self.description,
            "sourceCode": self.source_code,
        }
        if self.welcome:
            data.update(self.welcome.to_json())
        if self.preview:
            data["preview"] = self.preview.to_json()
        return data

    def from_json(self, data: Optional[JSONDict] = None) -> "BotInfo":
        super().from_json(data)
        if data is not None:
            self.commands = [
                BotCommand().from_json(x) for x in data.get("commands", [])
            ]
            self.description = data.get("description")
            self.welcome = BotWelcome(
                data.get("welcomeText"),
                data.get("buttonName"),
                data.get("buttonCommand"),
                data.get("welcomeImage"),
            )
            self.source_code = data.get("sourceCode")
            preview = data.get("preview")
            if isinstance(preview, str):
                preview = json.loads(preview)
            self.preview = AppPage.build_from_json(preview)

        return self

    def to_json(self) -> JSONDict:
        data = super().to_json()
        if not data.get("commands"):
            data["commands"] = [x.to_json() for x in self.commands]
        if not data.get("description"):
            data["description"] = self.description
        if self.welcome:
            data.update(self.welcome.to_json())
        if self.preview:
            data["preview"] = self.preview.to_json()
        return data
