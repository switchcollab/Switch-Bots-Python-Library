from typing import List
import swibots
from swibots.api.chat.models import Message


class GetFlagMessages:
    async def get_flag_messages(
        self: "swibots.ApiClient", user_id: int = None
    ) -> List[Message]:
        """Get flagged messages

        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The flagged messages

        Raises:
            ``~switch.error.SwitchError``: If the flagged messages could not be retrieved
        """
        return await self.chat_service.messages.get_flag_messages(user_id)
