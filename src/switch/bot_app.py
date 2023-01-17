import asyncio
import logging
from typing import List, Collection, Optional
import switch
from switch.api.community.events import CommunityEvent
from switch.api.chat.events import ChatEvent
from switch.bots import BotContext, Decorators, BaseHandler
from switch.api.common.events import Event
from .app import App

logger = logging.getLogger(f"{__name__}")


class BotApp(App, Decorators):
    """Bot client"""

    def __init__(
        self,
        token: str,
        bot_description: Optional[str] = None,
        auto_update_bot: Optional[bool] = True,
        loop: asyncio.AbstractEventLoop = None,
    ):
        """Initialize the client"""
        super().__init__(token, loop)
        self._user_type = switch.bots.Bot
        self.on_chat_service_start = self._on_chat_service_start
        self.on_community_service_start = self._on_community_service_start
        self._handlers: List[BaseHandler] = []
        self._register_commands: List[switch.bots.RegisterCommand] = []
        self._bot_description = bot_description
        self.auto_update_bot = auto_update_bot

    @property
    def bot(self) -> "switch.bots.Bot":
        return self.user

    @property
    def handlers(self) -> List[BaseHandler]:
        if self._handlers is None:
            self._handlers = []
        return self._handlers

    def register_command(
        self, command: switch.bots.RegisterCommand | List[switch.bots.RegisterCommand]
    ) -> "BotApp":
        if self._running:
            raise switch.SwitchError("Cannot register commands after the app has started")
        if isinstance(command, list):
            self._register_commands.extend(command)
        else:
            self._register_commands.append(command)
        return self

    def add_handler(self, handler: BaseHandler | List[BaseHandler]) -> "BotApp":
        if isinstance(handler, list):
            self.handlers.extend(handler)
        else:
            self.handlers.append(handler)
        return self

    async def _validate_token(self):
        await super()._validate_token()
        if not isinstance(self.user, switch.Bot):
            raise switch.SwitchError("Invalid token")

        if not self.user.is_bot:
            raise switch.SwitchError("Invalid token (not a bot)")

        self.user.app = self
        # Register commands
        await self.user.on_app_start(self)

    async def _on_chat_service_start(self, _):
        await self.chat_service.subscribe_to_notifications(callback=self.on_chat_event)

    async def _on_community_service_start(self, _):
        await self.community_service.subscribe_to_notifications(callback=self.on_community_event)

    def _build_context(self, event: Event) -> BotContext:
        return BotContext(bot=self.bot, event=event)

    async def process_event(self, ctx: BotContext):
        for handler in self.handlers:
            if await handler.should_handle(ctx):
                await handler.handle(ctx)
                break

    async def on_community_event(self, evt: CommunityEvent):
        if evt is not None and isinstance(evt, Event):
            await self.process_event(self._build_context(evt))

    async def on_chat_event(self, evt: ChatEvent):
        if evt is not None:
            await self.process_event(self._build_context(evt))