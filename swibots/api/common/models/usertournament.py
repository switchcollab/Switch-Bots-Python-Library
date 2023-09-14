import swibots
from typing import Optional
from swibots.base import SwitchObject
from swibots.utils.types import JSONDict


class UserTournament(SwitchObject):
    def __init__(
        self,
        app: Optional["swibots.App"] = None,
        id: Optional[str] = None,
        type: Optional[type] = None,
        name: Optional[str] = None,
        user_id: Optional[str] = None,
        xp_earned: Optional[int] = None,
    ):
        super().__init__(app)
        self.id = id
        self.type = type
        self.name = name
        self.user_id = user_id
        self.xp_earned = xp_earned

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "userId": self.user_id,
            "xpEarned": self.xp_earned,
        }

    @classmethod
    def from_json(self, data: JSONDict | None) -> "UserTournament":
        if data:
            self.id = data.get("id")
            self.type = data.get("type")
            self.name = data.get("name")
            self.user_id = data.get("userId")
            self.xp_earned = data.get("xpEarned")
        return self
