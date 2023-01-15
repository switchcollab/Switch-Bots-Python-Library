import asyncio
from contextlib import AbstractContextManager
import logging
from typing import Collection, List
from switch.bots import Bot, Command
from switch.api.common.events.event import Event
from switch.api.community.events.community_event import CommunityEvent
from switch.api.switch_client import SwitchClient
from switch.bots import BotContext
from switch.bots.handlers import (
    BaseHandler,
)
from switch.error import SwitchError

logger = logging.getLogger(f"{__name__}")


class SwitchApp(AbstractContextManager):
    def __init__(self, loop: asyncio.AbstractEventLoop = None):
        self._switch_client: SwitchClient = None
        self._loop = loop or asyncio.get_event_loop()
        self._bot: "Bot" = None
        self._handlers: Collection[BaseHandler] = []
        self._running = False
        self._description = None
        self._commands: List[Command] = []

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

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> "SwitchApp":
        self._description = value
        return self

    def command(self, command: str) -> "SwitchApp":
        self._commands.append(Command(command=command))
        return self

    @property
    def commands(self) -> List[Command]:
        return self._commands

    @commands.setter
    def commands(self, commands: List[Command]) -> "SwitchApp":
        self._commands = commands

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

            try:
                await (self.api.chat.start())
                await self.api.chat.subscribeToNotifications(callback=self.on_chat_event)
            except Exception as e:
                logger.exception(e)

            try:
                await (self.api.community.start())
                await self.api.community.subscribeToNotifications(callback=self.on_community_event)
            except Exception as e:
                logger.exception(e)

            # on app start hook
            for handler in self.handlers:
                await handler.on_app_start(self)

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

    def description(self, value: str) -> "SwitchAppBuilder":
        self._switch_app.description = value
        return self

    def commands(self, commands: List[Command] = []) -> "SwitchAppBuilder":
        for command in commands:
            self._switch_app.commands.append(command)
        return self

    def build(self) -> SwitchApp:
        self._switch_app.build()
        return self._switch_app
