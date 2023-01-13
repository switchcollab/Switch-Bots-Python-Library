import logging
from typing import TYPE_CHECKING, Type, TypeVar
from switch.api.auth.models.auth_user import AuthUser

if TYPE_CHECKING:
    from switch.api.auth import AuthClient

_logger = logging.getLogger(__name__)

BASE_PATH = "/user"
T = TypeVar("T", bound="AuthUser")


class UserController:
    def __init__(self, client: "AuthClient"):
        self.client = client

    async def me(self, user_type: Type[T] = AuthUser) -> T:
        response = await self.client.get(f"{BASE_PATH}")
        return user_type.build_from_json(response.data)
