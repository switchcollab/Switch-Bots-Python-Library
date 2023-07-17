import logging
from typing import TYPE_CHECKING
from datetime import timedelta, datetime

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/restrict"


class RestrictController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def restrict_user(
        self,
        community_id: str,
        restricted: bool,
        user_id: int,
        until_date: datetime | float | dict,
    ) -> bool:
        if isinstance(until_date, float):
            until_date = datetime.fromtimestamp(until_date)
        c_timestamp = isinstance(until_date, dict)

        response = await self.client.post(
            f"{BASE_PATH}/user",
            data={
                "communityId": community_id,
                "restricted": restricted,
                "restrictedTillTimestamp": until_date
                if c_timestamp
                else {
                    "day": until_date.day,
                    "month": until_date.month,
                    "year": until_date.year,
                },
                "userId": user_id,
            },
        )
        return response.data.get("success", False)

    async def update_restricted_user(
        self,
        community_id: str,
        restricted: bool,
        user_id: int,
        until_date: datetime | float | dict,
    ) -> bool:
        if isinstance(until_date, float):
            until_date = datetime.fromtimestamp(until_date)
        c_timestamp = isinstance(until_date, dict)
        response = await self.client.put(
            f"{BASE_PATH}/user",
            data={
                "communityId": community_id,
                "restricted": restricted,
                "restrictedTillTimestamp": until_date
                if c_timestamp
                else {
                    "day": until_date.day,
                    "month": until_date.month,
                    "year": until_date.year,
                },
                "userId": user_id,
            },
        )
        return response.data.get("success", False)
