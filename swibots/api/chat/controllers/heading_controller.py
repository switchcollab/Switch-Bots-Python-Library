import logging
from typing import TYPE_CHECKING, Optional, List, Literal
from swibots.api.community.models import CommunityHeading
from swibots.api.common.models import User
from urllib.parse import urlencode

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

class HeadingsController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def get_headings(self, community_id: str, additional: bool = False) -> List[CommunityHeading]:
        """
        :param community_id: The ID of the community
        :return: The Heading object
        """
        query = urlencode({"additional": additional,
                           "communityId": community_id,
                           })
        response = await self.client.get(f"/headings?{query}")
        return self.client.build_list(CommunityHeading, response.data)


    async def create_heading(self, community_id: str, name: str,
                             chat_id: str,
                             heading_for: Literal["CHANNEL", "GROUP"] = "CHANNEL",
                             heading_type: Literal['BLANK', "VALUE"] = "VALUE",
                             ):
        query = urlencode({
            "communityId": community_id,
            "heading": name,
            "id": chat_id,
            "headingFor": heading_for,
            "headingType": heading_type,
        })
        response = await self.client.post(f"/headings?{query}")
        return response.data

    async def delete_heading(self, community_id: str, heading_name: str):
        query = urlencode({
            "communityId": community_id,
            "headingName": heading_name,
        })
        response = await self.client.post(f"/headings/delete-headings?{query}")
        return response.data

    async def edit_heading(self, community_id: str, heading_name: str, new_heading_name: str,
                           heading_type: Literal['BLANK', "VALUE"] = "VALUE"):
        query = urlencode({
            "communityId": community_id,
            "headingName": heading_name,
            "newHeadingName": new_heading_name,
            "headingType": heading_type,
        })
        response = await self.client.post(f"/headings/edit-headings?{query}")
        return response.data

