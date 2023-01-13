import asyncio
from contextlib import AbstractContextManager
import functools
import json
import logging
import re
import signal
from typing import Collection
from switch.api.community.events.community_event import CommunityEvent
from switch.api.switch_client import SwitchClient
from switch.bots import BotContext, Bot
from switch.bots.events import CommandEvent, MessageEvent
from switch.bots.handlers import (
    BaseHandler,
)
from switch.error import SwitchError
from switch.utils.ws.common.ws_message import WsMessage
from switch.api.chat.models import Message
from switch.bots.constants import COMMAND_PARSER_REGEX

logger = logging.getLogger(f"{__name__}")


class SwitchApp(AbstractContextManager):
    def __init__(self, loop: asyncio.AbstractEventLoop = None):
        self._switch_client: SwitchClient = None
        self._loop = loop or asyncio.get_event_loop()
        self._bot: "Bot" = None
        self._handlers: Collection[BaseHandler] = []
        self._running = False

    @property
    def api(self) -> SwitchClient:
        if self._switch_client is None:
            self._switch_client = SwitchClient()
        return self._switch_client

    @property
    def bot(self) -> "Bot":
        return self._bot

    @property
    def handlers(self) -> Collection[BaseHandler]:
        if self._handlers is None:
            self._handlers = []
        return self._handlers

    def token(self, value: str) -> "SwitchApp":
        self.api.token = value
        return self

    def build(self):
        self.api.initialize()

    def add_handler(self, handler: BaseHandler):
        logger.debug("adding handler %s", handler)
        self.handlers.append(handler)

    async def _validate_token(self):
        # check if token is valid
        if self.api.token is None:
            raise SwitchError("Token is not set")

        try:
            logger.debug("checking token...")
            bot = await self.api.auth.users.me(user_type=Bot)
            self.api.user = bot
            logger.debug("token is valid %s", bot)
        except Exception as e:
            await self.stop()
            raise SwitchError("Invalid token")

        if self.api.user is None or not self.api.user.is_bot:
            raise SwitchError("Invalid token (not a bot token)")
        bot.app = self
        self._bot = bot

    async def _validate_run(self):
        await self._validate_token()

    def _build_context(self, event: Event) -> BotContext:
        return BotContext(bot=self.bot, event=event, app=self)

    async def process_event(self, ctx: BotContext):
        for handler in self.handlers:
            if await handler.should_handle(ctx):
                await handler.handle(ctx)
                break

    async def on_chat_message(self, raw_message: WsMessage):
        evt: Event = None
        # check if message is a command or a regular message
        if raw_message.body is not None and raw_message.body != "":
            json_data = json.loads(raw_message.body)
            if "message" in json_data and "type" in json_data and json_data["type"] == "Message":
                message = Message.build_from_json(json_data["message"]["msg"])
                if (
                    message.user_id == self.bot.id
                ):  # ignore messages from self to avoid infinite loop
                    return
                if re.match(COMMAND_PARSER_REGEX, message.message):
                    evt = CommandEvent(message)
                else:
                    evt = MessageEvent(message)

        if evt is not None:
            await self.process_event(self._build_context(evt))

    async def on_community_event(self, evt: CommunityEvent):
        if evt is not None and isinstance(evt, Event):
            await self.process_event(self._build_context(evt))

    async def on_chat_event(self, evt: Event):
        if evt is not None:
            await self.process_event(self._build_context(evt))

    async def start(self):
        try:

            if self._running:
                raise SwitchError("App is already running")
            self._running = True
            """Starts the app"""
            await self._validate_run()
            await (self.api.chat.start())
            await (self.api.community.start())

            await self.api.community.subscribeToNotifications(callback=self.on_community_event)
            await self.api.chat.subscribeToNotifications(callback=self.on_chat_event)

            # on app start hook
            for handler in self.handlers:
                await handler.on_app_start(self)

            await self.bot.on_app_start(self)

            # run forever
            while self._running:
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            self._running = False
            # await self._do_stop()

    async def _do_stop(self):
        logger.info("stopping app...")
        # on app stop hook
        for handler in self.handlers:
            await handler.on_app_stop(self)

        # await self.bot.on_app_stop(self)
        self._running = False

    async def stop(self):
        if not self._running:
            return
        await self._do_stop()

    def __enter__(self):
        return self.start()

    def __exit__(self, *args):
        try:
            self.stop()
        except ConnectionError:
            pass

    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self, *args):
        try:
            await self.stop()
        except ConnectionError:
            pass

    @staticmethod
    def builder() -> "SwitchAppBuilder":
        return SwitchAppBuilder()


class SwitchAppBuilder:
    def __init__(self):
        self._switch_app: SwitchApp = SwitchApp()

    def token(self, value: str) -> "SwitchAppBuilder":
        self._switch_app.token(value)
        return self

    def build(self) -> SwitchApp:
        self._switch_app.build()
        return self._switch_app
