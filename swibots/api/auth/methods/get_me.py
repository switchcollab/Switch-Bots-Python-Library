from typing import Type, TypeVar
import swibots
from swibots.api.common.models import User
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
        return await self.auth_service.get_me(user_type=user_type)

    async def update_user_info(self: "swibots.ApiClient", user_info: User) -> bool:
        """update_user_info

        Args:
            user_info (User): User info

        Returns:
            bool: Whether request was successful
        """
        data = {x: y for x, y in user_info.to_json_request().items() if y is not None}
        response = await self.auth_service.post(
            "/api/update/bot", data=data
        )
        return response.data