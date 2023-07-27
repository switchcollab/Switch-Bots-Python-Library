from typing import TYPE_CHECKING, List, Optional
from swibots.api.common.models import User
from swibots.utils.types import JSONDict
from .bot_command_info import BotCommandInfo


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
        commands: Optional[List[BotCommandInfo]] = None,
        description: Optional[str] = None,
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
        self.commands: List[BotCommandInfo] = commands or []
        self.description: Optional[str] = description

    def from_json(self, data: Optional[JSONDict] = None) -> "BotInfo":
        super().from_json(data)
        if data is not None:
            self.commands = [BotCommandInfo().from_json(x) for x in data.get("commands", [])]
            self.description = data.get("description")
        return self

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "commands": [x.to_json() for x in self.commands],
            "description": self.description,
        }
