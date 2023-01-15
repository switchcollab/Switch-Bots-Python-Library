import json
from typing import Tuple
from switch.api.auth.models.auth_user import AuthUser
from switch.api.chat.controllers import MessageController
from switch.api.chat.events import ChatEvent, CallbackQueryEvent, MessageEvent, CommandEvent
from switch.base import SwitchRestClient, SwitchWSAsyncClient
from switch.config import APP_CONFIG
from switch.error import SwitchError
from switch.types import EventType
from switch.utils.ws.asyncstomp.async_ws_subscription import AsyncWsSubscription
from switch.utils.ws.common.ws_message import WsMessage


class ChatClient(SwitchRestClient):
    def __init__(
        self,
        base_url: str = APP_CONFIG["CHAT_SERVICE"]["BASE_URL"],
        ws_url: str = APP_CONFIG["CHAT_SERVICE"]["WS_URL"],
    ):
        super().__init__(base_url)
        self._messages: MessageController = None
        self._bots: BotController = None
        self._authorization = None
        self._user: AuthUser = None
        self._ws: SwitchWSAsyncClient = None
        self._ws_url = ws_url

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
    def messages(self) -> MessageController:
        """Get the message controller"""
        if self._messages is None:
            self._messages = MessageController(self)
        return self._messages

    @property
    async def subscribe(self, endpoint: str, callback=None) -> AsyncWsSubscription:
        if self.user is None:
            raise SwitchError("User is not set")
        if callback is None:
            raise SwitchError("Callback is not set")
        return await self.ws.subscribe(endpoint, callback=callback)

    async def subscribeToNotifications(self, callback=None) -> AsyncWsSubscription:
        subscription = await self.ws.subscribe(
            "/chat/queue/events",
            callback=lambda event: callback(self._parse_event(event)),
        )
        return subscription

    def _parse_event(self, raw_message: WsMessage) -> ChatEvent:
        json_data = json.loads(raw_message.body)
        type = json_data.get("type", "MESSAGE")
        evt: ChatEvent = None
        if type == EventType.MESSAGE.value:
            evt = MessageEvent.build_from_json(json_data)
        elif type == EventType.COMMAND.value:
            evt = CommandEvent.build_from_json(json_data)
        elif type == EventType.CALLBACK_QUERY.value:
            evt = CallbackQueryEvent.build_from_json(json_data)
        else:
            evt = ChatEvent.build_from_json(json_data)
        return evt

    async def start(self):
        """Start the chat client"""
        if self.user is None:
            raise SwitchError("User is not set")
        await self.ws.connect()
        self._started = True

    async def stop(self):
        if self._started:
            await self.ws.disconnect()
            self._started = False
