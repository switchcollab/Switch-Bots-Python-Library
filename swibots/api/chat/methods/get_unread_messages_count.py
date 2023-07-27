import swibots


class GetUnreadMessagesCount:
    async def get_unread_messages_count(self: "swibots.ApiClient") -> int:
        """Get the amount of unread messages

        Returns:
            ``int``: The amount of unread messages

        Raises:
            ``~switch.error.SwitchError``: If the amount of unread messages could not be retrieved

        This method does the same as :meth:`~switch.api.chat.controllers.MessageController.get_unread_messages_count`.
        """
        return await self.chat_service.messages.get_unread_messages_count()
