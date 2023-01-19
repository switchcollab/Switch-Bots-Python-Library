from typing import Type, TypeVar
import swibots
from swibots.api.bot.models import BotInfo


class GetBotInfo:
    async def get_bot_info(self: "swibots.ApiClient", bot_id: str) -> BotInfo:
        """Get bot info

        Parameters:
            bot_id (``str``): The bot id. Defaults to the current bot id.

        Returns:
            :obj:``~switch.api.bot.models.BotInfo``: The bot info

        This functions does the same as :meth:`~switch.api.bot.controllers.BotController.get_bot_info`.
        """
        return await self.bots_service.bots.get_bot_info(bot_id=bot_id)
