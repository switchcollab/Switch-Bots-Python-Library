import logging
from typing import TYPE_CHECKING, Type, TypeVar
from switch.api.auth.models.user import User

if TYPE_CHECKING:
    from switch.api.auth import AuthClient

_logger = logging.getLogger(__name__)

BASE_PATH = "/user"
T = TypeVar("T", bound="User")


class UserController:
    def __init__(self, client: "AuthClient"):
        self.client = client

    async def me(self, user_type: Type[T] = User) -> T:
        response = await self.client.get(f"{BASE_PATH}")
        return user_type.from_json(response.data)
