from typing import Type, TypeVar
import swibots
from swibots.api.chat.models import Message


class DeleteMessagesFromUser:
    async def delete_messages_from_user(self: "swibots.ApiClient", user_id: int) -> bool:
        """Delete all messages from a user

        Parameters:
            user_id (``int``): The user id

        Returns:
            ``bool``: Whether the messages were deleted

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be deleted

        This method does the same as :meth:`~switch.api.chat.controllers.MessageController.delete_messages_from_user`.
        """
        return await self.chat_service.messages.delete_messages_from_user(user_id)
