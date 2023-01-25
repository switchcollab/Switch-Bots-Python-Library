import logging
import swibots
from typing import TYPE_CHECKING, Type, TypeVar
from ..models import AuthUser

if TYPE_CHECKING:
    from swibots.api.auth import AuthClient

log = logging.getLogger(__name__)

BASE_PATH = "/user"
T = TypeVar("T", bound="AuthUser")


class UserController:
    """User controller

    This controller is used to communicate with the user endpoints.

    """

    def __init__(self, client: "AuthClient"):
        self.client = client

    async def me(self, user_type: Type[T] = AuthUser) -> T:
        """Get the current user

        Parameters:
            user_type (``Type[T]``, *optional*): The user type to return. Defaults to :obj:`~switch.api.auth.models.AuthUser`.

        Returns:
            ``T``: The current user

        """
        response = await self.client.get(f"{BASE_PATH}")
        return self.client.build_object(user_type, response.data)
