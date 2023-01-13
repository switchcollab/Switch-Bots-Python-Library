from typing import Optional
from switch.utils.types import JSONDict
from switch.base.switch_object import SwitchObject


class User(SwitchObject):
    __slots__ = (
        "id",
        "name",
        "username",
        "image_url",
        "active",
        "deleted",
        "role_info",
        "admin",
        "bot",
    )

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
        bot: Optional[bool] = None,
    ):
        self.id = id
        self.name = name
        self.username = username
        self.image_url = image_url
        self.active = active
        self.deleted = deleted
        self.role_info = role_info
        self.admin = admin
        self.bot = bot

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "imageUrl": self.image_url,
            "active": self.active,
            "deleted": self.deleted,
            "roleInfo": self.role_info,
            "admin": self.admin,
            "bot": self.bot,
        }

    def from_json(self, data: Optional[JSONDict] = None) -> "User":
        if data is not None:
            self.id = data.get("id")
            self.name = data.get("name")
            self.username = data.get("username")
            self.image_url = data.get("imageUrl")
            self.active = data.get("active")
            self.deleted = data.get("deleted")
            self.role_info = data.get("roleInfo")
            self.admin = data.get("admin")
            self.bot = data.get("bot")
        return self
