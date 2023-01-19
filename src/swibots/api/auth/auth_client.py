from swibots.api.auth.controllers import UserController
from swibots.base import SwitchRestClient
from swibots.config import APP_CONFIG


class AuthClient(SwitchRestClient):
    """Auth client

    This client is used to communicate with the auth service.

    Controllers:
        - :attr:`users`: :obj:`~switch.api.auth.controllers.UserController` : The users controller
    """

    def __init__(self, base_url: str = APP_CONFIG["AUTH_SERVICE"]["BASE_URL"]):
        super().__init__(base_url)
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
        if self._auth_token is not None:
            headers["authtoken"] = f"{self._auth_token}"
        return headers
