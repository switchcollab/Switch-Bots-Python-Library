from swibots.api.auth.controllers import UserController
from swibots.base import SwitchRestClient
from swibots.config import get_config
import swibots


class AuthClient(SwitchRestClient):
    """Auth client

    This client is used to communicate with the auth service.

    Controllers:
        - :attr:`users`: :obj:`~switch.api.auth.controllers.UserController` : The users controller
    """

    def __init__(self, app: "swibots.App", base_url: str = None):
        """Initialize the auth client"""
        base_url = base_url or get_config()["AUTH_SERVICE"]["BASE_URL"]
        super().__init__(app, base_url)
        self._users = None
        self._authorization = None

    @property
    def users(self) -> UserController:
        """Get the users controller

        Returns:
            :obj:`~switch.api.auth.controllers.UserController`: The users controller
        """
        if self._users is None:
            self._users = UserController(self)
        return self._users

    def prepare_request_headers(self, headers: dict) -> dict:
        headers = super().prepare_request_headers(headers)
        if self.token is not None:
            headers["authtoken"] = f"{self.token}"
        return headers
