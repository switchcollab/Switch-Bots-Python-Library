from typing import Type, TypeVar
import swibots
from swibots.api.bot.models import BotInfo


class UpdateBotInfo:
    async def update_bot_info(self: "swibots.ApiClient", bot_info: BotInfo) -> BotInfo:
        """Update bot info

        Parameters:
            bot_info (``~switch.api.bot.models.BotInfo``): The bot info to update

        Returns:
            :obj:``~switch.api.bot.models.BotInfo``: The bot info

        This functions does the same as :meth:`~switch.api.bot.controllers.BotController.update_bot_info`.
        """
        return await self.bots_service.bots.update_bot_info(bot_info=bot_info)
