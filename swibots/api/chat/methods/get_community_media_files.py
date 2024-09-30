from typing import List
import swibots
from swibots.api.chat.models import Message
from typing import Literal, Union
from swibots.api.community.models import Channel, Group, SearchResultUser


class GetCommunityMediaFiles:
    async def get_community_media_files(
        self: "swibots.ApiClient", community_id: str
    ) -> List[Message]:
        """Get community media files

        Parameters:
            community_id (``int``): The community id

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved

        This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_messages`.
        """
        return await self.chat_service.messages.get_community_media_files(community_id)

    async def search_community_data(
        self: "swibots.ApiClient",
        query: str,
        community_id: str,
        filter: Literal[
            "MESSAGE", "MEDIA", "LINK", "GROUP", "CHANNEL", "MEMBER"
        ] = "MESSAGE",
        limit: int = 10,
        page: int = 0,
    ) -> Union[List[Message], List[Group], List[Channel], List[SearchResultUser]]:
        """Search community data

        Parameters:
            query (``str``): The search query
            community_id (``str``): The community id
            filter (``str``, *optional*): The filter. Defaults to "MESSAGES".
            limit (``int``, *optional*): The limit. Defaults to 10.
            page (``int``, *optional*): The page. Defaults to 0.

        Returns:
            Union[List[Message], List[Group], List[Channel], List[SearchResultUser]]: The search results

        Raises:
            ``~switch.error.SwitchError``: If the search results could not be retrieved
        """
        return await self.chat_service.messages.search_community_data(
            query, community_id, filter, limit, page
        )
