import swibots
from typing import Optional

from swibots.api.community.models import InstantMessaging


class InstantMessagingMethods:
    async def enable_messages(
        self: "swibots.ApiClient",
        community_id: str,
        group_id: str,
        bot_id: Optional[str] = None,
    ) -> InstantMessaging:
        """Enable messaging in group"""
        return await self.community_service.instantmessaging.enable_messages(
            community_id, group_id, bot_id
        )

    async def disable_messages(
        self: "swibots.ApiClient",
        community_id: str,
        group_id: str,
        bot_id: Optional[str] = None,
    ) -> InstantMessaging:
        """Disable messaging in group"""
        return await self.community_service.instantmessaging.disable_messages(
            community_id, group_id, bot_id
        )

    async def get_messaging_enabled(
        self: "swibots.ApiClient", community_id: str, group_id: str
    ) -> InstantMessaging:
        """Get bot with messaging enable in the community"""
        return await self.community_service.instantmessaging.get_messaging_enabled(
            community_id, group_id
        )
