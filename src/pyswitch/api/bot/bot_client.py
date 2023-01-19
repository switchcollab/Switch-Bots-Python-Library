from pyswitch.api.auth.models.auth_user import AuthUser
from pyswitch.api.bot.controllers import BotController
from pyswitch.base import SwitchRestClient
from pyswitch.config import APP_CONFIG


class BotClient(SwitchRestClient):
    """Bot client

    This client is used to communicate with the bot service.

    Controllers:
        - :attr:`bots`: :obj:`~switch.api.bot.controllers.BotController` : The bot controller

    Properties:
        - :attr:`user`: :obj:`~switch.api.auth.models.auth_user.AuthUser` : The current user

    """

    def __init__(self, base_url: str = APP_CONFIG["BOT_SERVICE"]["BASE_URL"]):
        """Initialize the bot client

        Parameters:
            base_url (``str``): The base url of the bot service. Defaults to the value in the config.
        """
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
