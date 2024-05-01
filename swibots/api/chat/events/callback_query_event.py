from typing import Optional, Literal
import swibots
from swibots.api.common.events.event import Event
from swibots.api.community.models.channel import Channel
from swibots.api.community.models.community import Community
from swibots.api.community.models.group import Group
from swibots.api.common.models.user import User
from swibots.api.callback import AppPage
from swibots.api.callback import CallbackResponse
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
        details: Optional[CallbackResponse] = None,
        app_session_id: Optional[str] = None,
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
        self.details = details
        self.app_session_id = app_session_id

    def from_json(self, data: JSONDict) -> "CallbackQueryEvent":
        super().from_json(data)
        if data is not None:
            self.callback_data = self.data.get("callbackData")
            self.query_id = self.data.get("callbackQueryId")
            self.details = CallbackResponse().from_json(
                self.data.get("message", {}).get("additionalDetails")
            )
            self.app_session_id = self.data.get("message", {}).get("appSessionId")
        return self

    async def __action_callback(self, **kwargs):
        resp = await self.app.bots_service.post(
            "/v1/bots/callback/answer",
            data={
                "type": "action_callback",
                "callbackQueryId": self.query_id,
                "messageId": str(self.message.id),
                **kwargs,
            },
        )
        return resp.data

    async def share(self, text: str):
        """Prompt a user to share text"""
        return await self.__action_callback(action="share", url=text)

    async def copy(self, text: str):
        """Copy text to user's clipboard.

        text (str): text which should be copied to user's device."""
        return await self.__action_callback(action="copy", url=text)

    async def redirect(self, url: str):
        """Redirect user to external url.

        url (str): url to open"""
        return await self.__action_callback(action="navigate", url=url)

    async def show_ad(
        self,
        id: str,
        ad_type: Literal["VIDEO_1", "VIDEO_2"],
        success_callback: str = None,
    ):
        """Display ad to the user on any callback action.

        id: session id to join.
        ad_type: either 'VIDEO_1' or 'VIDEO_2'
        success_callback: Callback to trigger after successfully showing.
        """
        return await self.__action_callback(
            action="show_ad",
            addId=id,
            addType=ad_type,
            extraOptions={"onAdUpdate": success_callback},
        )

    async def request_session_join(self,
                                   session_id: str):
        """Request user to join the session, from session id
        
        session_id: (str)
        """
        return await self.__action_callback(
            url=session_id,
            action="joinSession"
        )

    async def request_session_create(self,
                                   callback_data: str = None):
        """Create the bot session on the behalf of user.

        callback_data: str: Callback data to trigger after creating"""
        return await self.__action_callback(
            url=callback_data,
            action="createSession"
        )


    async def answer(
        self,
        text: str = None,
        url: Optional[str] = None,
        show_alert: Optional[bool] = False,
        cache_time: Optional[int] = None,
        callback: Optional[AppPage] = None,
        new_page: bool = False,
    ) -> bool:
        """Answer callback query"""
        if callback:
            query_id = self.query_id
            if not new_page and self.details.parent_id:
                query_id = self.details.parent_id
            return await self.app.answer_ui_query(
                query_id,
                callback=callback,
                message_id=self.message.id,
                app_session_id=self.app_session_id,
            )
        return await self.app.answer_callback_query(
            self.query_id,
            message_id=self.message.id,
            text=text,
            url=url,
            show_alert=show_alert,
            cache_time=cache_time,
            app_session_id=self.app_session_id,
        )
