import logging
from typing import Type, TypeVar, List, Union
import swibots
from swibots.api.chat.models import Message


class DeleteMessage:
    async def delete_message(self: "swibots.ApiClient", message: int | Message) -> bool:
        """Delete a message

        Parameters:
            message (``int`` | ``~switch.api.chat.models.Message``): The message to delete

        Returns:
            ``bool``: Whether the message was deleted

        Raises:
            ``~switch.error.SwitchError``: If the message could not be deleted

        This method does the same as :meth:`~switch.api.chat.controllers.MessageController.delete_message`.
        """
        logging.warning(
            "This method is deprecated and is going to be removed in the future! Use client.delete_messages to achieve same results!"
        )
        return await self.chat_service.messages.delete_messages([message])

    async def delete_messages(
        self: "swibots.ApiClient", message_ids: List[Union[int, Message]]
    ) -> bool:
        """Delete one or more messages.

        This method allows you to delete one or more messages from a chat.

        Parameters:
            message_ids (List[Union[int, Message]]): A list of message IDs or Message objects to delete.

        Returns:
            bool: True if the messages were deleted successfully, False otherwise.

        Raises:
            SwitchError: If the messages could not be deleted.

        Note:
            This method internally calls the :meth:`~switch.api.chat.controllers.MessageController.delete_message` method.

        Example:
            >>> client = Client(...)
            >>> message_ids = [1, 2, 3]
            >>> result = await client.delete_messages(message_ids)
            >>> print(result)
            True
        """
        return await self.chat_service.messages.delete_messages(message_ids=message_ids)
