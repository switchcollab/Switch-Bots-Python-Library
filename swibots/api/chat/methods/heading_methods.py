from typing import Type, TypeVar, Optional, List, Literal
import swibots
from swibots.api.community.models import CommunityHeading


class HeadingMethods:

    async def get_headings(
        self: "swibots.ApiClient", community_id: str, additional: bool = False
    ) -> List[CommunityHeading]:
        """
        Get the headings of a community

        :param community_id: The ID of the community
        :param additional: Whether to get additional information about the headings
        """
        return await self.chat_service.headings.get_headings(community_id, additional)

    async def create_heading(
        self: "swibots.ApiClient",
        community_id: str,
        name: str,
        chat_id: str,
        heading_for: Literal["CHANNEL", "GROUP"] = "CHANNEL",
        heading_type: Literal["BLANK", "VALUE"] = "VALUE",
    ):
        """
        Create a heading in a community

        :param community_id: The ID of the community
        :param name: The name of the heading
        :param chat_id: The ID of the chat
        :param heading_for: The type of the heading
        :param heading_type: The type of the heading
        """
        return await self.chat_service.headings.create_heading(
            community_id, name, chat_id, heading_for, heading_type
        )

    async def delete_heading(self, community_id: str, heading_name: str):
        """
        Delete a heading from a community

        :param community_id: The ID of the community
        :param heading_name: The name of the heading to delete
        """
        return await self.chat_service.headings.delete_heading(
            community_id, heading_name
        )

    async def edit_heading(
        self,
        community_id: str,
        heading_name: str,
        new_heading_name: str,
        heading_type: Literal["BLANK", "VALUE"] = "VALUE",
    ):
        """
        Edit a heading in a community

        :param community_id: The ID of the community
        :param heading_name: The name of the heading to edit
        :param new_heading_name: The new name of the heading
        :param heading_type: The type of the heading
        """
        return await self.chat_service.headings.edit_heading(
            community_id, heading_name, new_heading_name, heading_type
        )
