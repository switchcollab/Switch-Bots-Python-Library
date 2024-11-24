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

    async def rearrange_headings(
        self: "swibots.ApiClient",
        community_id: str,
        heading_names: List[str],
        subheading: str = ''
    ):
        """
        Rearrange headings in a community

        :param community_id: The ID of the community
        :param heading_names: List of heading names in the desired order
        :param subheading: Optional subheading name
        """
        return await self.chat_service.headings.rearrange_headings(
            community_id, heading_names, subheading
        )

    async def move_heading_content(
        self,
        community_id: str,
        heading_for: Literal["GROUP", "CHANNEL", "STORE", "WIDGET"],
        heading_type: Literal["BLANK", "VALUE"],
        type_id: str,
        updated_heading: str
    ):
        """
        Move content from one heading to another

        :param community_id: The ID of the community
        :param heading_for: The type of content being moved
        :param heading_type: The type of heading
        :param type_id: The ID of the content being moved
        :param updated_heading: The name of the heading to move content to
        """
        move_dto = {
            "communityId": community_id,
            "headingFor": heading_for,
            "headingType": heading_type,
            "typeId": type_id,
            "updatedHeading": updated_heading
        }
        request_dto = {"moveHeadingContentDto": [move_dto]}
        return await self.chat_service.headings.move_heading_content(request_dto)
