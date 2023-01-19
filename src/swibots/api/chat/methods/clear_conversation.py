from typing import Type, TypeVar
import swibots
from swibots.api.chat.models import Message


class ClearConversation:
    async def clear_conversation(self: "swibots.ApiClient", receiver_id: int) -> bool:
        """Clear a conversation

        Parameters:
            receiver_id (``int``): The receiver id

        Returns:
            ``bool``: True if the conversation was cleared

        Raises:
            ``~switch.error.SwitchError``: If the conversation could not be cleared

        This method does the same as :meth:`~switch.api.chat.controllers.MessageController.clear_conversation`.
        """
        return await self.chat_service.messages.clear_conversation(receiver_id)
