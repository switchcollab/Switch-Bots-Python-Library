import swibots

from datetime import datetime
from swibots.api.community.models import Channel

class RestrictUser:

    """
    Class for restricting users in a community.

    Args:
        api_client (swibots.ApiClient): The API client to use.

    Methods:
        restrict_user(community_id, restricted, user_id, until_date):
            Restricts a user in a community.
        update_restricted_user(community_id, restricted, user_id, until_date):
            Updates the restriction status of a user in a community.
    """

    async def restrict_user(
        self: "swibots.ApiClient",
        community_id: str,
        restricted: bool,
        user_id: int,
        until_date: int = 0,
    ) -> bool:
        """
        Restricts a user in a community.

        Args:
            community_id (str): The ID of the community.
            restricted (bool): Whether the user should be restricted.
            user_id (int): The ID of the user to restrict.
            until_date (int): The timestamp until which the user should be restricted.

        Returns:
            bool: Whether the restriction was successful.
        """

        return await self.community_service.restrict.restrict_user(
            community_id=community_id,
            restricted=restricted,
            user_id=user_id,
            until_date=until_date,
        )

    async def update_restricted_user(
        self: "swibots.ApiClient",
        community_id: str,
        restricted: bool,
        user_id: int,
        until_date: int = 0,
    ) -> bool:
        """
        Updates the restriction status of a user in a community.

        Args:
            community_id (str): The ID of the community.
            restricted (bool): Whether the user should be restricted.
            user_id (int): The ID of the user to restrict.
            until_date (float | int): The date until which the user should be restricted.

        Returns:
            bool: Whether the restriction update was successful.
        """

        return await self.community_service.restrict.update_restricted_user(
            community_id, restricted, user_id, until_date
        )

    async def get_restricted_user(self: "swibots.ApiClient", community_id: str, user_id:int):
        """get restricted user from community_id and user_id"""
        return await self.community_service.restrict.get_restricted_user(community_id, user_id)