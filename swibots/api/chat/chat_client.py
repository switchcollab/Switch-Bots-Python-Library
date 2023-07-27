import json
import logging
from typing import Tuple
from swibots.api.auth.models.auth_user import AuthUser
from swibots.api.chat.controllers import MessageController
from swibots.api.chat.events import ChatEvent, CallbackQueryEvent, MessageEvent, CommandEvent, InlineQueryEvent
from swibots.base import SwitchRestClient, SwitchWSAsyncClient
from swibots.config import get_config
from swibots.error import SwitchError
from swibots.types import EventType
from swibots.utils.ws.asyncstomp.async_ws_subscription import AsyncWsSubscription
from swibots.utils.ws.common.ws_message import WsMessage
import swibots

logger = logging.getLogger(__name__)


class ChatClient(SwitchRestClient):
    """Chat client

    This client is used to communicate with the chat service.

    Controllers:
        - :attr:`messages`: :obj:`~switch.api.chat.controllers.MessageController` : The message controller

    Properties:
        - :attr:`user`: :obj:`~switch.api.auth.models.auth_user.AuthUser` : The current user
        - :attr:`ws`: :obj:`~switch.base.SwitchWSAsyncClient` : The websocket client

    """

    def __init__(
        self,
        app: "swibots.App" = None,
        base_url: str = None,
        ws_url: str = None,
    ):
        """Initialize the chat client

        Parameters:
            base_url (``str``): The base url of the chat service. Defaults to the value in the config.
            ws_url (``str``): The websocket url of the chat service. Defaults to the value in the config.
        """
        base_url = base_url or get_config()["CHAT_SERVICE"]["BASE_URL"]
        self._ws_url = ws_url or get_config()["CHAT_SERVICE"]["WS_URL"]
        super().__init__(app, base_url)
        self._messages: MessageController = None
        self._ws: SwitchWSAsyncClient = None
        self._started = False

    @property
    def ws(self) -> SwitchWSAsyncClient:
        if self._ws is None:
            self._ws = SwitchWSAsyncClient(self._ws_url, self.token)
        return self._ws

    @property
    def messages(self) -> MessageController:
        """Get the message controller"""
        if self._messages is None:
            self._messages = MessageController(self)
        return self._messages

    async def subscribe(self, endpoint: str, callback=None) -> AsyncWsSubscription:
        """Subscribe to a websocket endpoint

        Parameters:
            endpoint (``str``): The endpoint to subscribe to
            callback (``callable``): The callback to call when a message is received

        Returns:
            :obj:`~switch.utils.ws.asyncstomp.async_ws_subscription.AsyncWsSubscription`: The subscription

        Raises:
            :obj:`~switch.error.SwitchError`: If the user is not set or the callback is not set
        """
        if self.user is None:
            raise SwitchError("User is not set")
        if callback is None:
            raise SwitchError("Callback is not set")
        return await self.ws.subscribe(endpoint, callback=callback)

    async def subscribe_to_notifications(self, callback=None) -> AsyncWsSubscription:
        """Subscribe to the notification endpoint

        Parameters:
            callback (``callable``): The callback to call when a message is received

        Returns:
            :obj:`~switch.utils.ws.asyncstomp.async_ws_subscription.AsyncWsSubscription`: The subscription

        Raises:
            :obj:`~switch.error.SwitchError`: If the user is not set or the callback is not set

        This is a shortcut for :meth:`subscribe` with the endpoint set to ``/chat/queue/events``
        """
        subscription = await self.ws.subscribe(
            "/chat/queue/events",
            callback=lambda event: callback(self._parse_event(event)),
        )
        return subscription

    def _parse_event(self, raw_message: WsMessage) -> ChatEvent:
        try:
            json_data = json.loads(raw_message.body)
            type = json_data.get("type", "MESSAGE")
            evt: ChatEvent = None
            if type == EventType.MESSAGE.value:
                evt = self.build_object(MessageEvent, json_data)
                # evt = MessageEvent.build_from_json(json_data)
            elif type == EventType.COMMAND.value:
                evt = self.build_object(CommandEvent, json_data)
                # evt = CommandEvent.build_from_json(json_data)
            elif type == EventType.CALLBACK_QUERY.value:
                evt = self.build_object(CallbackQueryEvent, json_data)
                # evt = CallbackQueryEvent.build_from_json(json_data)
            elif type == EventType.INLINE_QUERY.value:
                evt = self.build_object(InlineQueryEvent, json_data)
            else:
                evt = self.build_object(ChatEvent, json_data)
                # evt = ChatEvent.build_from_json(json_data)
            return evt
        except Exception as e:
            logger.exception(e)

    async def start(self):
        """Start the chat websocket client
        Raises:
            :obj:`~switch.error.SwitchError`: If the user is not set
        """
        if self.user is None:
            raise SwitchError("User is not set")
        await self.ws.connect()
        self._started = True

    async def stop(self):
        """Stop the chat websocket client"""
        if self._started:
            await self.ws.disconnect()
            self._started = False
