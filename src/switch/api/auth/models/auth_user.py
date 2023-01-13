from typing import Optional
from switch.base.switch_object import SwitchObject


class AuthUser(SwitchObject):
    __slots__ = (
        "id",
        "username",
    )

    def __init__(self, username: Optional[str] = None, id: Optional[int] = None):
        self.id = id
        self.username = username
