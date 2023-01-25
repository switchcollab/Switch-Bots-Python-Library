from swibots.api.auth.models.auth_user import AuthUser
from swibots.api.bot.controllers import BotController
from swibots.base import SwitchRestClient
from swibots.config import get_config
import swibots


class BotClient(SwitchRestClient):
    """Bot client

    This client is used to communicate with the bot service.

    Controllers:
        - :attr:`bots`: :obj:`~switch.api.bot.controllers.BotController` : The bot controller

    Properties:
        - :attr:`user`: :obj:`~switch.api.auth.models.auth_user.AuthUser` : The current user

    """

    def __init__(self, app: "swibots.App" = None, base_url: str = None):
        """Initialize the bot client

        Parameters:
            base_url (``str``): The base url of the bot service. Defaults to the value in the config.
        """
        base_url = base_url or get_config()["BOT_SERVICE"]["BASE_URL"]
        super().__init__(app, base_url)
        self._bots: BotController = None

    @property
    def bots(self) -> BotController:
        """Get the bot controller"""
        if self._bots is None:
            self._bots = BotController(self)
        return self._bots
