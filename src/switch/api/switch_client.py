from switch.api.auth.auth_client import AuthClient
from switch.api.auth.models.user import User
from .chat import ChatClient

class SwitchClient(object):
    def __init__(self, **kwargs):
        """Initialize the client"""
        self._token:str = None
        self.__dict__.update(kwargs)
        self._chat_client:ChatClient = None
        self._auth_client:AuthClient = None
        self._user:User = None

    async def initialize(self):
        """Initialize the client"""
        await self.chat.initialize()
        await self.auth.initialize()
    
    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User):
        self._user = value
        if self._chat_client is not None:
            self._chat_client.user = value
    
    @property
    def token(self) -> str:
        """Get the token"""
        return self._token
    
    @token.setter
    def token(self, value: str):
        """Set the token"""
        self._token = value
        if self._chat_client is not None:
            self._chat_client.token = value
        if self._auth_client is not None:
            self._auth_client.token = value

    @property
    def chat(self) -> ChatClient:
        """Get the chat client"""
        if self._chat_client is None:
            self._chat_client = ChatClient()
            self._chat_client.token = self.token
            self._chat_client.user = self.user
        return self._chat_client

    @property
    def auth(self) -> AuthClient:
        """Get the auth client"""
        if self._auth_client is None:
            self._auth_client = AuthClient()
            self._auth_client.token = self.token
        return self._auth_client

   
      