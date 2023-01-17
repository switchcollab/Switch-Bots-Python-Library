import json
import logging
from typing import TYPE_CHECKING, List
from switch.api.bot.models import BotInfo, BotCommandInfo
from switch.error import SwitchError
from switch.utils.types import JSONDict

if TYPE_CHECKING:
    from switch.api.bot import BotClient

_logger = logging.getLogger(__name__)

BASE_PATH = "/v1/bots"


class BotController:
    """Bot controller

    This controller is used to communicate with the bot endpoints.
    """

    def __init__(self, client: "BotClient"):
        self.client = client

    async def get_bot_info(self, bot_id: str) -> BotInfo:
        """Get bot info

        Parameters:
            bot_id (``str``): The bot id. Defaults to the current bot id.

        Returns:
            :obj:``~switch.api.bot.models.BotInfo``: The bot info
        """
        if bot_id is None:
            bot_id = self.client.user.id
        response = await self.client.get(f"{BASE_PATH}/{bot_id}")
        return BotInfo.build_from_json(response.data)

    async def update_bot_info(self, bot_info: BotInfo) -> BotInfo:
        """Update bot info

        Parameters:
            bot_info (``~switch.api.bot.models.BotInfo``): The bot info to update

        Returns:
            :obj:``~switch.api.bot.models.BotInfo``: The bot info
        """
        data = bot_info.to_json_request()
        response = await self.client.put(f"{BASE_PATH}", data=data)
        return BotInfo.build_from_json(response.data)

    async def delete_bot_info(self, bot_id: str) -> bool:
        """Delete bot info

        Parameters:
            bot_id (``str``): The bot id. Defaults to the current bot id.

        Returns:
            ``bool``: True if the bot was deleted
        """
        response = await self.client.delete(f"{BASE_PATH}/{bot_id}")
        return True