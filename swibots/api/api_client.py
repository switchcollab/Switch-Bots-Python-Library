import swibots
from .auth import AuthClient
from .chat import ChatClient
from .community import CommunityClient
from .bot import BotClient
from .auth.models import AuthUser
from .airdrop import AirdropClient

from .auth.methods import AuthMethods
from .bot.methods import BotMethods
from .chat.methods import ChatMethods
from .community.methods import CommunityMethods
from .airdrop.methods import AirdropMethods

class ApiClient(
    AuthMethods,
    BotMethods,
    ChatMethods,
    CommunityMethods,
    AirdropMethods
):
    def __init__(self, **kwargs):
        """Initialize the client"""
        self._token: str = None
        self.__dict__.update(kwargs)
        self._chat_client: ChatClient = None
        self._auth_client: AuthClient = None
        self._community_client: CommunityClient = None
        self._bot_client: BotClient = None
        self._user: AuthUser = None
        self._airdrop_client: AirdropClient = None
        self.initialize()

    def initialize(self):
        """Initialize the client"""
        self.chat_service.initialize()
        self.auth_service.initialize()
        self.community_service.initialize()

    @property
    def user(self) -> AuthUser:
        return self._user

    @user.setter
    def user(self, value: AuthUser):
        self._user = value

    @property
    def token(self) -> str:
        """Get the token"""
        return self._token

    @token.setter
    def token(self, value: str):
        """Set the token"""
        self._token = value

    @property
    def chat_service(self) -> ChatClient:
        """Get the chat client"""
        if self._chat_client is None:
            self._chat_client = ChatClient(self)
        return self._chat_client

    @property
    def auth_service(self) -> AuthClient:
        """Get the auth client"""
        if self._auth_client is None:
            self._auth_client = AuthClient(self)
        return self._auth_client

    @property
    def community_service(self) -> CommunityClient:
        """Get the community client"""
        if self._community_client is None:
            self._community_client = CommunityClient(self)
        return self._community_client

    @property
    def airdrop_service(self) -> AirdropClient:
        """Get the airdrop client"""
        if self._airdrop_client is None:
            self._airdrop_client = AirdropClient(self)
        return self._airdrop_client

    @property
    def bots_service(self) -> BotClient:
        """Get the bot client"""
        if self._bot_client is None:
            self._bot_client = BotClient(self)
        return self._bot_client
