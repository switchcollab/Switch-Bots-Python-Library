import json
import logging
from typing import Tuple, Optional, List
from swibots.api.chat.controllers import (
    MessageController,
    ChatController,
    MediaController,
    StickerController,
)
from swibots.api.chat.events import (
    ChatEvent,
    CallbackQueryEvent,
    MessageEvent,
    CommandEvent,
    InlineQueryEvent,
)
from swibots.base import SwitchRestClient, SwitchWSAsyncClient
from swibots.config import get_config
from swibots.errors import SwitchError
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
        self._post: ChatController = None
        self._media: MediaController = None
        self._stickers: StickerController = None
        self._ws: SwitchWSAsyncClient = None
        self._started = False

    @property
    def ws(self) -> SwitchWSAsyncClient:
        if self._ws is None:
            self._ws = SwitchWSAsyncClient(self._ws_url, self.token)
        return self._ws

    @property
    def stickers(self) -> StickerController:
        if self._stickers is None:
            self._stickers = StickerController(self)
        return self._stickers

    @property
    def messages(self) -> MessageController:
        """Get the message controller"""
        if self._messages is None:
            self._messages = MessageController(self)
        return self._messages

    @property
    def posts(self) -> ChatController:
        """Get the post controller"""
        if self._post is None:
            self._post = ChatController(self)
        return self._post

    @property
    def media(self) -> MediaController:
        """Gets the media controller"""
        if self._media is None:
            self._media = MediaController(self)
        return self._media

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
        return await self.ws.subscribe(
            "/chat/queue/events",
            callback=lambda event: self._parse_event(event, callback),
        )

    async def _parse_event(self, raw_message: WsMessage, callback) -> ChatEvent:
        try:
            json_data = json.loads(raw_message.body)
            messagetype = json_data.get("type", "MESSAGE")
            evt: ChatEvent = None
            if messagetype == EventType.MESSAGE.value:
                evt = self.build_object(MessageEvent, json_data)
                if not (evt.message.community_id or evt.message.receiver_id != "null"):
                    logger.debug(
                        f"recieved message event with incorrect data: {evt.to_json()}"
                    )
                    return
                # evt = MessageEvent.build_from_json(json_data)
            elif messagetype == EventType.COMMAND.value:
                evt = self.build_object(CommandEvent, json_data)
                if not (evt.message.community_id or evt.message.receiver_id != "null"):
                    logger.debug(
                        f"recieved command event with incorrect data: {evt.to_json()}"
                    )
                    return
                # evt = CommandEvent.build_from_json(json_data)
            elif messagetype == EventType.CALLBACK_QUERY.value:
                evt = self.build_object(CallbackQueryEvent, json_data)
                # evt = CallbackQueryEvent.build_from_json(json_data)
            elif messagetype == EventType.INLINE_QUERY.value:
                evt = self.build_object(InlineQueryEvent, json_data)
            else:
                evt = self.build_object(ChatEvent, json_data)
                # evt = ChatEvent.build_from_json(json_data)
        except Exception as e:
            logger.exception(e)
            return

        return await callback(evt)

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
        if self._started and self.ws:
            await self.ws.disconnect()
            self._started = False
