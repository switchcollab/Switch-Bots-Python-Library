import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

from swibots.api.chat.models import Organization, OrgApp
from swibots.api.common import User
from urllib.parse import urlencode

log = logging.getLogger(__name__)

BASE_PATH = "/v1/organization"


class OrganizationController:
    """Organization controller"""

    def __init__(self, client: "ChatClient") -> None:
        self.client = client

    async def get_organizations(
        self, bot_id: int = None, community_id: str = None, user_id: str = None
    ):
        param = urlencode(
            {"botId": bot_id, "communityId": community_id, "userId": user_id}
        )
        response = await self.client.get(f"{BASE_PATH}/get-organizations?{param}")
        return self.client.build_list(Organization, response.data)

    async def get_organization_by_id(self, id: str):
        response = await self.client.get(f"{BASE_PATH}/{id}")
        return self.client.build_object(Organization, response.data)

    async def get_organization_apps(self, id: str):
        response = await self.client.get(f"{BASE_PATH}/apps?orgId={id}")
        return self.client.build_list(OrgApp, response.data)

    async def get_organization_followers(self, id: str):
        response = await self.client.get(f"{BASE_PATH}/followers?orgId={id}")
        return self.client.build_list(User, response.data)
