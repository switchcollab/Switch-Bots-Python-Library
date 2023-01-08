from switch.api.auth.controllers import UserController
from switch.utils import SwitchRestClient

BASE_URL = 'http://51.159.11.53:9999/api'

class AuthClient(SwitchRestClient):
    def __init__(self):
        super().__init__(BASE_URL)
        self._users = None
        self._authorization = None
    
    def users(self) -> UserController:
        """Get the users controller"""
        if self._users is None:
            self._users = UserController(self)
        return self._users

    def prepare_request_headers(self, headers: dict) -> dict:
        headers= super().prepare_request_headers(headers)
        if self._auth_token is not None:
            headers['authtoken'] = f'{self._auth_token}'
        return headers