from typing import Type, TypeVar
import switch
from switch.api.chat.models import Message
from switch.api.community.models import Group, Channel


class ForwardMessage:
    async def forward_message(
        self: "switch.ApiClient",
        message: Message | int,
        group_channel: Group | Channel | str = None,
        receiver_id: str = None,
    ) -> Message:
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
            message, group_channel, receiver_id
        )