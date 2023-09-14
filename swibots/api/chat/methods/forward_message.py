from typing import Type, TypeVar, Optional, List
import swibots
from swibots.api.chat.models import Message
from swibots.api.community.models import Group, Channel


class ForwardMessage:
    async def forward_message(
        self: "swibots.ApiClient",
        message_id: int | List[int],
        group_channel: Optional[Group | Channel | str] = None,
        user_id: Optional[int] = None,
    ) -> Message | List[Message]:
        """Forward a message

        Parameters:
            message (``~switch.api.chat.models.Message`` | ``int``): The message to forward
            group_channel (``~switch.api.community.models.Group`` | ``~switch.api.community.models.Channel`` | ``str``): The group/channel to forward the message to
            receiver_id (``str``): The receiver id to forward the message to

        Returns:
            ``~switch.api.chat.models.Message``: The forwarded message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be forwarded

        This functions does the same as :meth:`~switch.api.chat.controllers.MessageController.forward_message`.
        """
        return await self.chat_service.messages.forward_message(
            message_id, group_channel, user_id
        )
