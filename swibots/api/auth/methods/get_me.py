from typing import Type, TypeVar
import swibots
from swibots.api.auth.models import AuthUser

T = TypeVar("T", bound="swibots.AuthUser")


class GetMe:
    async def get_me(self: "swibots.ApiClient", user_type: Type[T] = AuthUser) -> T:
        """Get the current user

        Parameters:
            user_type (``Type[T]``, *optional*): The user type to return. Defaults to :obj:`~switch.api.auth.models.AuthUser`.

        Returns:
            ``T``: The current user

        This functions does the same as :meth:`~switch.api.auth.controllers.UserController.me`.

        """
        return await self.auth_service.users.me(user_type=user_type)
