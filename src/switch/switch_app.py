import asyncio
import json
import logging
import re
from typing import Collection
from switch.api.switch_client import SwitchClient
from switch.bots import BaseHandler, BotContext, Event, Bot, CommandEvent, MessageEvent
from switch.error import SwitchError
from switch.utils.ws.common.ws_message import WsMessage
from switch.api.chat.models import Message
from switch.bots.constants import EventType, COMMAND_PARSER_REGEX

logger = logging.getLogger(f"{__name__}")


class SwitchApp:
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
                message = Message.from_json(json_data["message"]["msg"])
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

    async def run(self):
        try:
            if self._running:
                raise SwitchError("App is already running")
            self._running = True
            """Starts the app"""
            await self._validate_run()
            self._loop.create_task(self.api.chat.run(on_message=self.on_chat_message))

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
            print("Tasks has been canceled")

    async def _do_stop(self):
        # on app stop hook
        for handler in self.handlers:
            await handler.on_app_stop(self)

        # await self.bot.on_app_stop(self)
        self._running = False
        self._loop.stop()

    async def stop(self):
        if not self._running:
            return
        await self._do_stop()

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
