from switch.api.auth.models.auth_user import AuthUser
from switch.api.bot.controllers import BotController
from switch.base import SwitchRestClient
from switch.config import APP_CONFIG


class BotClient(SwitchRestClient):
    def __init__(self, base_url: str = APP_CONFIG["BOT_SERVICE"]["BASE_URL"]):
        super().__init__(base_url)
        self._bots: BotController = None
        self._authorization = None
        self._user: AuthUser = None

    @property
    def user(self) -> AuthUser:
        return self._user

    @user.setter
    def user(self, value: AuthUser):
        self._user = value

    @property
    def bots(self) -> BotController:
        """Get the bot controller"""
        if self._bots is None:
            self._bots = BotController(self)
        return self._bots
