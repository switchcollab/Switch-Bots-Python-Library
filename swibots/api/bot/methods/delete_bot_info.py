from typing import Type, TypeVar
import swibots


class DeleteBotInfo:
    async def delete_bot_info(self: "swibots.ApiClient", bot_id: str) -> bool:
        """Delete bot info

        Parameters:
            bot_id (``str``): The bot id. Defaults to the current bot id.

        Returns:
            ``bool``: True if the bot info was deleted

        This functions does the same as :meth:`~switch.api.bot.controllers.BotController.delete_bot_info`.
        """
        return await self.bots_service.bots.delete_bot_info(bot_id=bot_id)
