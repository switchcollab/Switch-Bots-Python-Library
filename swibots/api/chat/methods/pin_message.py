from typing import TYPE_CHECKING, Type, TypeVar, Optional
import swibots
from swibots.api.chat.models import Message

if TYPE_CHECKING:
    from swibots.api import ApiClient


class PinMessage:
    async def pin_message(
        self: "ApiClient",
        message: Message | int,
        detail: Optional[str] = None,
        message_type: Optional[str] = None,
    ) -> bool:
        """pin a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to edit

        Raises:
            ``~switch.error.SwitchError``: If the message could not be pinned

        This method does the same as :meth:`~switch.api.chat.controllers.PostController.pin_message`.
        """
        return await self.chat_service.posts.pin_message(
            message, detail=detail, message_type=message_type
        )
