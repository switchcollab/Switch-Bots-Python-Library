from typing import Type, TypeVar, List
import swibots
from swibots.api.chat.models import ADInfo


class AdMethods:
    async def get_all_ads(
        self: "swibots.ApiClient", limit: int = 100, page: int = 0
    ) -> List[ADInfo]:
        """Get all ads created by the user

        Parameters:
            page (``int``): The page number to offset.
            limit (``int``): The number of result to include.

        Returns:
            List[ADInfo]
        """
        return await self.chat_service.ads.get_all_ads(page=page, limit=limit)
