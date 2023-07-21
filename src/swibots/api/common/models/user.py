from typing import Optional, List, Any
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject


class User(SwitchObject):
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        username: Optional[str] = None,
        image_url: Optional[str] = None,
        active: Optional[bool] = None,
        deleted: Optional[bool] = None,
        role_info: Optional[str] = None,
        admin: Optional[bool] = None,
        is_bot: Optional[bool] = None,
        tournaments: Optional[List[Any]] = None
    ):
        self.id = id
        self.name = name
        self.username = username
        self.image_url = image_url
        self.active = active
        self.deleted = deleted
        self.role_info = role_info
        self.admin = admin
        self.is_bot = is_bot
        self.tournaments = tournaments

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
            "is_bot": self.is_bot,
            "tournamentsParticipated": self.tournaments
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
            self.is_bot = data.get("is_bot") or data.get("bot")
        return self
