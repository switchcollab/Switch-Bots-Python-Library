import swibots

from swibots.api.community.models import CommunityMember


class GetCommunityMember:
    async def get_community_member(self: "swibots.ApiClient", community_id: str, user_id: str) -> CommunityMember:
        """Get a community member.

        Args:
            community_id: The ID of the community.
            user_id: The ID of the user.

        Returns:
            The community member.
        """
        return await self.community_service.communities.get_community_member(community_id, user_id)
