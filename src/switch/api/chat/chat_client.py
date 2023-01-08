from typing import Tuple
from switch.api.auth.models.user import User
from switch.api.chat.controllers import MessageController
from switch.utils import SwitchRestClient

BASE_URL = 'http://51.158.56.0:8080'

class ChatClient(SwitchRestClient):
    def __init__(self):
        super().__init__(BASE_URL)
        self._messages = None
        self._authorization = None
        self._user:User = None

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User):
        self._user = value

    
    def messages(self) -> MessageController:
        """Get the message controller"""
        if self._messages is None:
            self._messages = MessageController(self)
        return self._messages