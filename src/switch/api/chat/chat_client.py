from typing import Tuple
from switch.api.auth.models.user import User
from switch.api.chat.controllers import MessageController
from switch.base import SwitchRestClient, SwitchWSAsyncClient
from switch.config import APP_CONFIG
from switch.error import SwitchError


class ChatClient(SwitchRestClient):
    def __init__(
        self,
        base_url: str = APP_CONFIG["CHAT_SERVICE"]["BASE_URL"],
        ws_url: str = APP_CONFIG["CHAT_SERVICE"]["WS_URL"],
    ):
        super().__init__(base_url)
        self._messages = None
        self._authorization = None
        self._user: User = None
        self._ws: SwitchWSAsyncClient = None
        self._ws_url = ws_url

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User):
        self._user = value

    @property
    def ws(self) -> SwitchWSAsyncClient:
        if self._ws is None:
            self._ws = SwitchWSAsyncClient(self._ws_url)
            self._ws.token = self._auth_token
        return self._ws

    @property
    def messages(self) -> MessageController:
        """Get the message controller"""
        if self._messages is None:
            self._messages = MessageController(self)
        return self._messages

    async def run(self, on_message=None):
        """Start the chat client"""
        await self.ws.connect()
        if self.user is None:
            raise SwitchError("User is not set")
        await self.ws.subscribe("/topic/listen." + str(self.user.id), callback=on_message)
