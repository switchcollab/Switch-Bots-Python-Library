from typing import Optional
import swibots
from swibots.api.common.events.event import Event
from swibots.api.community.models.channel import Channel
from swibots.api.community.models.community import Community
from swibots.api.community.models.group import Group
from swibots.api.common.models.user import User
from swibots.api.chat.models.message import Message
from swibots.types import EventType
from swibots.utils.types import JSONDict
from .command_event import CommandEvent


class CallbackQueryEvent(CommandEvent):
    """Message event"""

    def __init__(
        self,
        app: "swibots.App" = None,
        type: Optional[EventType] = None,
        community_id: Optional[str] = None,
        community: Optional[Community] = None,
        group_id: Optional[str] = None,
        group: Optional[Group] = None,
        channel_id: Optional[str] = None,
        channel: Optional[Channel] = None,
        action_by_id: Optional[int] = None,
        action_by: Optional[User] = None,
        data: Optional[dict] = None,
        user_id: Optional[str] = None,
        user: Optional[User] = None,
        message: Optional[Message] = None,
        command: Optional[str] = None,
        params: Optional[str] = None,
        callback_data: Optional[JSONDict] = None,
        query_id: Optional[str] = None,
    ):
        super().__init__(
            app=app,
            type=type or EventType.CALLBACK_QUERY,
            community_id=community_id,
            community=community,
            group_id=group_id,
            group=group,
            channel_id=channel_id,
            channel=channel,
            action_by_id=action_by_id,
            action_by=action_by,
            data=data,
            user_id=user_id,
            user=user,
            message=message,
            command=command,
            params=params,
        )
        self.callback_data = callback_data
        self.query_id = query_id

    def from_json(self, data: JSONDict) -> "CallbackQueryEvent":
        super().from_json(data)
        if data is not None:
            self.callback_data = self.data.get("callbackData")
            self.query_id = self.data.get("callbackQueryId")
            return self

    async def answer(
        self,
        text: str,
        url: Optional[str] = None,
        show_alert: Optional[bool] = False,
        cache_time: Optional[int] = None,
    ) -> bool:
        """Answer callback query"""
        return await self.app.answer_callback_query(
            self.query_id,
            text=text,
            url=url,
            show_alert=show_alert,
            cache_time=cache_time,
        )
