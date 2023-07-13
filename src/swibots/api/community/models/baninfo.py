from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
import swibots


class BanInfo(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        banned: Optional[bool] = None,
        message: Optional[str] = None,
    ):
        super().__init__(app)
        self.banned = banned
        self.message = message

    def to_json(self) -> JSONDict:
        return {"isBanned": self.banned, "message": self.message}

    @classmethod
    def from_json(self, data: JSONDict | None) -> "BanInfo":
        if data is not None:
            self.banned = data.get("isBanned")
            self.message = data.get("message")
        return self
