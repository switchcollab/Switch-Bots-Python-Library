import json
from switch.api.auth.models.auth_user import AuthUser
from switch.api.community.events import *
from switch.base import SwitchRestClient, SwitchWSAsyncClient
from switch.config import APP_CONFIG
from switch.error import SwitchError
from switch.utils.ws.asyncstomp.async_ws_subscription import AsyncWsSubscription
from switch.utils.ws.common.ws_message import WsMessage
from switch.types import EventType


class CommunityClient(SwitchRestClient):
    def __init__(
        self,
        base_url: str = APP_CONFIG["COMMUNITY_SERVICE"]["BASE_URL"],
        ws_url: str = APP_CONFIG["COMMUNITY_SERVICE"]["WS_URL"],
    ):
        super().__init__(base_url)
        self._messages = None
        self._authorization = None
        self._user: AuthUser = None
        self._ws: SwitchWSAsyncClient = None
        self._ws_url = ws_url
        self._started = False

    @property
    def user(self) -> AuthUser:
        return self._user

    @user.setter
    def user(self, value: AuthUser):
        self._user = value

    @property
    def ws(self) -> SwitchWSAsyncClient:
        if self._ws is None:
            self._ws = SwitchWSAsyncClient(self._ws_url)
            self._ws.token = self._auth_token
        return self._ws

    @property
    async def subscribe(self, endpoint: str, callback=None) -> AsyncWsSubscription:
        if self.user is None:
            raise SwitchError("User is not set")
        if callback is None:
            raise SwitchError("Callback is not set")
        return await self.ws.subscribe(endpoint, callback=callback)

    async def subscribe_to_notifications(self, callback=None) -> AsyncWsSubscription:
        subscription = await self.ws.subscribe(
            "/user/queue/events",
            callback=lambda event: callback(self._parse_event(event)),
        )
        return subscription

    def _parse_event(self, raw_message: WsMessage) -> CommunityEvent:
        json_data = json.loads(raw_message.body)
        type = json_data.get("type", "COMMUNITY")

        if type == EventType.CHANNEL_CREATE.value:
            return ChannelCreatedEvent.build_from_json(json_data)
        elif type == EventType.CHANNEL_UPDATE.value:
            return ChannelUpdatedEvent.build_from_json(json_data)
        elif type == EventType.CHANNEL_DELETE.value:
            return ChannelDeletedEvent.build_from_json(json_data)
        elif type == EventType.COMMUNITY_UPDATE.value:
            return CommunityUpdatedEvent.build_from_json(json_data)
        elif type == EventType.GROUP_CREATE.value:
            return GroupCreatedEvent.build_from_json(json_data)
        elif type == EventType.GROUP_UPDATE.value:
            return GroupUpdatedEvent.build_from_json(json_data)
        elif type == EventType.GROUP_DELETE.value:
            return GroupDeletedEvent.build_from_json(json_data)
        elif type == EventType.USER_BAN.value:
            return UserBannedEvent.build_from_json(json_data)
        elif type == EventType.MEMBER_JOIN.value:
            return MemberJoinedEvent.build_from_json(json_data)
        elif type == EventType.MEMBER_LEAVE.value:
            return MemberLeftEvent.build_from_json(json_data)

        return CommunityEvent.build_from_json(json_data)

    async def start(self):
        """Start the community client"""
        if self.user is None:
            raise SwitchError("User is not set")
        await self.ws.connect()
        self._started = True

    async def stop(self):
        if self._started:
            await self.ws.disconnect()
            self._started = False
