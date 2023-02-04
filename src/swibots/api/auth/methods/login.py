from typing import Type, TypeVar
import swibots
from swibots.api.auth.models import AuthUser

T = TypeVar("T", bound="swibots.AuthUser")


class Login:
    async def login(self: "swibots.ApiClient", username: str, password: str, user_type: Type[T] = AuthUser) -> T:
        """Login with username and password

        Parameters:
            username (``str``): The username   
            password (``str``): The password
            user_type (``Type[T]``, *optional*): The user type to return. Defaults to :obj:`~switch.api.auth.models.AuthUser`.

        Returns:
            ``T``: The user

        This functions does the same as :meth:`~switch.api.auth.controllers.UserController.login`.
        
        
        """
        return await self.auth_service.users.login(username=username, password=password, user_type=user_type)
