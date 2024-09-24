from typing import Optional, List
from swibots.base.switch_object import SwitchObject
from swibots.utils.types import JSONDict


class AuthResult(SwitchObject):
    def __init__(
        self,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        user_id: Optional[int] = None,
        is_bot: Optional[bool] = False,
        roles: Optional[List[str]] = None,
        active: Optional[bool] = False,
    ):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.user_id = user_id
        self.is_bot = is_bot
        self.roles = roles
        self.active = active

    def from_json(self, data: Optional[JSONDict]) -> "AuthResult":
        super().from_json(data)
        if data is not None:
            self.access_token = data.get("access_token")
            self.refresh_token = data.get("refresh_token")
            self.user_id = data.get("user_id")
            self.is_bot = data.get("is_bot")
            self.roles = data.get("roles")
            self.active = data.get("active")
        return self
