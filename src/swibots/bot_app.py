import asyncio
import logging
from typing import List, Collection, Optional
import swibots
from swibots.api.community.events import CommunityEvent
from swibots.api.chat.events import ChatEvent
from swibots.bots import BotContext, Decorators, BaseHandler
from swibots.api.common.events import Event
from .app import App

log = logging.getLogger(f"{__name__}")


class BotApp(App, Decorators):
    """Bot client

    This is the main class for interacting with the Switch BOT API.

    """

    def __init__(
        self,
        # username: Optional[str] = None,
        # password: Optional[str] = None,
        token: Optional[str] = None,
        bot_description: Optional[str] = None,
        auto_update_bot: Optional[bool] = True,
        loop: asyncio.AbstractEventLoop = None,
    ):
        """
        Initialize the client

        Args:
            token (:obj:`str`): The bot token.
            bot_description(:obj:`str`): The bot description.
            auto_update_bot(:obj:`bool`): Whether to automatically update the bot description and the regitered commands.
            loop (:obj:`asyncio.AbstractEventLoop`): The asyncio loop to use (default: asyncio.get_event_loop()).

        """
        super().__init__(token, loop)
        self._user_type = swibots.bots.Bot
        self.on_chat_service_start = self._on_chat_service_start
        self.on_community_service_start = self._on_community_service_start
        self._handlers: List[BaseHandler] = []
        self._register_commands: List[swibots.bots.RegisterCommand] = []
        self._bot_description = bot_description
        self.auto_update_bot = auto_update_bot

    @property
    def bot(self) -> "swibots.bots.Bot":
        """
        The bot user.

            Returns:
                :obj:`swibots.bots.Bot`: The bot user.
        """
        return self.user

    @property
    def handlers(self) -> List[BaseHandler]:
        """
        Get the list of handlers.

        Returns:
            :obj:`List[BaseHandler]`: The list of handlers.
        """
        if self._handlers is None:
            self._handlers = []
        return self._handlers

    def register_command(
        self, command: swibots.bots.RegisterCommand | List[swibots.bots.RegisterCommand]
    ) -> "BotApp":
        if self._running:
            raise swibots.SwitchError(
                "Cannot register commands after the app has started")
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

    def remove_handler(self, handler: BaseHandler | List[BaseHandler]) -> "BotApp":
        if isinstance(handler, list):
            for h in handler:
                self.handlers.remove(h)
        else:
            self.handlers.remove(handler)
        return self

    async def _validate_token(self):
        await super()._validate_token()
        if not isinstance(self.user, swibots.Bot):
            raise swibots.SwitchError("Invalid token")

        if not self.user.is_bot:
            raise swibots.SwitchError("Invalid token (not a bot)")

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
                try:
                    await handler.handle(ctx)
                except Exception as e:
                    log.exception(f"Error while processing event: {e}")
                    raise e
                finally:
                    break

    async def on_community_event(self, evt: CommunityEvent):
        if evt is not None and isinstance(evt, Event):
            await self.process_event(self._build_context(evt))

    async def on_chat_event(self, evt: ChatEvent):
        if evt is not None:
            await self.process_event(self._build_context(evt))
