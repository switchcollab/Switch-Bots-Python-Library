import swibots
from typing import List

from swibots.api.common.models import User
from swibots.api.chat.models import Organization, OrgApp

class OrganizationMethods:
    """Organization methods.

    This class provides methods for interacting with organizations in a chat application.

    Methods:
        get_organizations: Retrieve a list of organizations based on specified parameters.
        get_organization_by_id: Retrieve details of an organization by its ID.
        get_organization_apps: Retrieve the apps associated with a specific organization.
        get_organization_followers: Retrieve the followers of a specific organization.
    """

    async def get_organizations(
        self: "swibots.ApiClient",
        bot_id: int = None,
        community_id: str = None,
        user_id: str = None,
    ) -> List[Organization]:
        """Get a list of organizations.

        Args:
            bot_id (int, optional): The ID of the bot associated with the organizations.
            community_id (str, optional): The ID of the community associated with the organizations.
            user_id (str, optional): The ID of the user associated with the organizations.

        Returns:
            List[Organization]: A list of Organization objects.
        """
        return await self.chat_service.organization.get_organizations(
            bot_id=bot_id, community_id=community_id, user_id=user_id
        )

    async def get_organization_by_id(self: "swibots.ApiClient", id: str) -> List[Organization]:
        """Get organization details by ID.

        Args:
            id (str): The ID of the organization.

        Returns:
            Organization: The Organization object.
        """
        return await self.chat_service.organization.get_organization_by_id(id)

    async def get_organization_apps(self: "swibots.ApiClient", id: str) -> List[OrgApp]:
        """Get apps associated with an organization.

        Args:
            id (str): The ID of the organization.

        Returns:
            OrgApp: The OrgApp object.
        """
        return await self.chat_service.organization.get_organization_apps(id)

    async def get_organization_followers(self: "swibots.ApiClient", id: str) -> List[User]:
        """Get followers of an organization.

        Args:
            id (str): The ID of the organization.

        Returns:
            List[User]: A list of User objects representing followers.
        """
        return await self.chat_service.organization.get_organization_followers(id)
