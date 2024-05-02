import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

from swibots.api.chat.models import ADInfo
from swibots.api.common import User
from urllib.parse import urlencode

log = logging.getLogger(__name__)

BASE_PATH = "/add"


class AdvertisingController:
    """Ads controller"""

    def __init__(self, client: "ChatClient") -> None:
        self.client = client

    async def get_all_ads(
        self, limit: int = 100, page: int = 0,
    ):
        param = urlencode(
            {"page": page, "limit": limit, "appId": self.client.user.id}
        )
        response = await self.client.get(f"{BASE_PATH}/byAppId?{param}")
        return self.client.build_list(ADInfo, response.data)

    async def get_organization_followers(self, id: str):
        response = await self.client.get(f"{BASE_PATH}/followers?orgId={id}")
        return self.client.build_list(User, response.data)
