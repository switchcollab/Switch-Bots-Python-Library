import swibots

from typing import List, Optional
from swibots.api.community.models import CommunityMember, Community


class CommunityMethods:
    async def get_community_member(
        self: "swibots.ApiClient", community_id: str, user_id: str
    ) -> CommunityMember:
        """Get a community member.

        Args:
            community_id: The ID of the community.
            user_id: The ID of the user.

        Returns:
            The community member.
        """
        return await self.community_service.communities.get_community_member(
            community_id, user_id
        )

    async def get_community_members(
        self: "swibots.ApiClient", community_id: str
    ) -> List[CommunityMember]:
        """Get community members"""
        return await self.community_service.communities.get_community_members(
            community_id
        )

    async def get_community(
        self: "swibots.ApiClient", id: str = "", username: str = ""
    ) -> Community:
        """Get a community by its ID or username

        Args:
            id (`str`): The ID of the community
            username (`str`): Username of the community

        Returns:
            :obj:`swibots.api.community.models.Community`: The community object.

        Raises:
            :obj:`switch.error.SwitchError`: If the community could not be retrieved
            :obj:`ValueError`: if the community id and username is provided together.

        This method does the same as :meth:`switch.api.community.controllers.CommunityController.get_community`.
        """
        return await self.community_service.communities.get_community(
            id, username=username
        )

    async def is_admin(
        self: "swibots.ApiClient", community_id: str, user_id: int
    ) -> bool:
        """Check if the user is admin of the community

        Args:
          community_id (str): Community ID
          user_id (int): User id
        """
        return await self.community_service.communities.is_admin(
            community_id, user_id=user_id
        )

    async def get_active_commands(
        self: "swibots.ApiClient",
        community_id: str,
        channel_id: Optional[str] = None,
        group_id: Optional[str] = None,
    ):
        """Get Active commands in the community

        Args:
            community_id (str): Community ID
            channel_id (Optional[str], optional): Channel ID
            group_id (Optional[str], optional): Group ID. Defaults to None.

        Returns:
            _type_: _description_
        """
        return await self.community_service.communities.get_active_commands(
            community_id=community_id, group_id=group_id, channel_id=channel_id
        )

    async def approve_chat_join(
        self: "swibots.ApiClient",
        members: List[int],
        community_id: str,
        channel_id: Optional[str] = None,
        group_id: Optional[str] = None,
    ):
        """Approve private join request

        Args:
          members: List[user_id]
          community_id: Community ID
          group_id: the group id
          channel_id: the channel id
        """
        return await self.community_service.communities.approve_chat_join(
            members,
            community_id=community_id,
            group_id=group_id,
            channel_id=channel_id,
        )

    async def decline_chat_join(
        self: "swibots.ApiClient",
        members: List[int],
        community_id: str,
        channel_id: Optional[str] = None,
        group_id: Optional[str] = None,
    ):
        """Decline private join request

        Args:
          members: List[user_id]
          community_id: Community ID
          group_id: the group id
          channel_id: the channel id
        """
        return await self.community_service.communities.approve_chat_join(
            members,
            community_id=community_id,
            group_id=group_id,
            channel_id=channel_id,
            decline=True,
        )
