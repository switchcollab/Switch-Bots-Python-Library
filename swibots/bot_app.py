import re, httpx
import os, signal
import asyncio
import logging
import shutil
from contextlib import AbstractContextManager
from typing import List, Optional, Callable
import swibots
from contextlib import suppress
from signal import signal as signal_fn, SIGINT, SIGTERM, SIGABRT
from io import BytesIO
from swibots.bots import Bot
from importlib import import_module
from swibots.errors import SwitchError, CancelError
from swibots.api.community.events import CommunityEvent
from swibots.api.chat.events import ChatEvent
from swibots.bots import BotContext, Decorators, BaseHandler
from swibots.api.bot.models import BotInfo, BotCommand
from swibots.api.common.events import Event
from swibots.utils import (
    DownloadProgress,
    IOClient,
    RestClient,
    DownloadProgressCallback,
)
from swibots.api import ApiClient

log = logging.getLogger(__name__)
LoaderLog = logging.getLogger("loader")
# Signal number to name
signals = {
    k: v
    for v, k in signal.__dict__.items()
    if v.startswith("SIG") and not v.startswith("SIG_")
}


class Client(Decorators, AbstractContextManager, ApiClient):
    """Bot client

    This is the main class for interacting with the Switch BOT API.

    """

    def __init__(
        self,
        token: str,
        bot_description: Optional[str] = None,
        auto_update_bot: Optional[bool] = True,
        loop: asyncio.AbstractEventLoop = None,
        receive_updates: Optional[bool] = True,
    ):
        """
        Initialize the client

        Args:
            token (:obj:`str`): The bot token.
            bot_description(:obj:`str`): The bot description.
            auto_update_bot(:obj:`bool`): Whether to automatically update the bot description and the regitered commands.
            loop (:obj:`asyncio.AbstractEventLoop`): The asyncio loop to use (default: asyncio.get_event_loop()).

        """
        super().__init__()
        self.token = token
        self._user_type = Bot
        self._botinfo: BotInfo = None
        self.on_app_start = None
        self.on_app_stop = None
        self.on_chat_service_start = self._on_chat_service_start
        self.on_community_service_start = self._on_community_service_start
        self._handlers: List[BaseHandler] = []
        self._register_commands: List[BotCommand] = []
        self._bot_description = bot_description
        #        self._plugins = plugins
        self.auto_update_bot = auto_update_bot
        self._loop = loop or asyncio.get_event_loop()
        self.user = self._loop.run_until_complete(
            self.get_me(user_type=self._user_type)
        )
        self._bot_id = self.user.id
        self._running = False
        self._user_type = Bot
        self.rest_client = RestClient()
        self.receive_updates = receive_updates

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

    def __loadModule(self, path):
        baseName = os.path.basename(path)
        if baseName.startswith("__") or not baseName.endswith(".py"):
            return
        try:
            module_path = path[:-3].replace("\\", ".").replace("/", ".")

            return import_module(module_path)
        except Exception as er:
            LoaderLog.exception(er)

    def load_plugins(self, plugins: List[str]):
        for path in plugins:
            if os.path.isfile(path):
                self.__loadModule(path)
                return
            for root, __, files in os.walk(path):
                for f in files:
                    self.__loadModule(os.path.join(root, f))

    def set_bot_commands(self, command: BotCommand | List[BotCommand]) -> "BotApp":
        if isinstance(command, list):
            self._register_commands.extend(command)
        else:
            self._register_commands.append(command)
        asyncio.run_coroutine_threadsafe(self.update_bot_commands(), self._loop)
        return self

    def delete_bot_commands(self, command: BotCommand | List[BotCommand]) -> "BotApp":
        if isinstance(command, list):
            for cmd in command:
                self._register_commands.remove(cmd)
        else:
            self._register_commands.remove(command)
        asyncio.run_coroutine_threadsafe(self.update_bot_commands(), self._loop)
        return self

    def add_handler(self, handler: BaseHandler | List[BaseHandler]) -> "BotApp":
        if isinstance(handler, list):
            self.handlers.extend(handler)
        else:
            self.handlers.append(handler)
        return self

    def remove_handler(self, handler: BaseHandler | List[BaseHandler]) -> "BotApp":
        if not isinstance(handler, list):
            handler = [handler]
        for h in handler:
            self.handlers.remove(h)
        return self

    async def update_bot_commands(self):
        # get all app commands
        commands = self._register_commands or []
        description = self._bot_description or ""
        # register the commands
        self._botinfo = BotInfo(
            description=description, id=self._bot_id, commands=commands
        )

        self._botinfo = await self.update_bot_info(self._botinfo)

    async def _validate_token(self):
        await super()._validate_token()
        if not isinstance(self.user, self._user_type):
            raise swibots.SwitchError("Invalid token")

        if not self.user.is_bot:
            raise swibots.SwitchError("Invalid token (not a bot)")

        self.user.app = self
        # Register commands
        await self.user.on_app_start(self)

    async def _on_chat_service_start(self, _):
        await self.chat_service.subscribe_to_notifications(callback=self.on_chat_event)

    async def _on_community_service_start(self, _):
        await self.community_service.subscribe_to_notifications(
            callback=self.on_community_event
        )

    def _build_context(self, event: Event) -> BotContext:
        return BotContext(app=self, event=event)

    async def process_event(self, ctx: BotContext):
        for handler in self.handlers:
            try:
                #                print(handler)
                await handler.handle(ctx)
            except Exception as e:
                log.exception(f"Error while processing event: {e}")
                raise e

    async def on_community_event(self, evt: CommunityEvent):
        if evt is not None and isinstance(evt, Event):
            await self.process_event(self._build_context(evt))

    async def on_chat_event(self, evt: ChatEvent):
        if evt is not None:
            await self.process_event(self._build_context(evt))

    async def handle_download(
        self,
        url: str,
        file_name: str,
        directory="downloads/",
        in_memory: bool = False,
        block: bool = True,
        progress: DownloadProgressCallback = None,
        progress_args: tuple = (),
    ):
        if directory is None or directory == "":
            directory = "downloads/"
        if not in_memory:
            os.makedirs(directory, exist_ok=True)
        temp_file_path = (
            os.path.abspath(re.sub("\\\\", "/", os.path.join(directory, file_name)))
            + ".temp"
        )
        file = BytesIO() if in_memory else open(temp_file_path, "wb")

        dProgress = DownloadProgress(
            total=0,
            downloaded=0,
            file_name=file_name,
            client=IOClient(),
            url=url,
        )

        if progress:
            await progress(dProgress, *progress_args)
        try:
            with self.rest_client.stream("GET", url) as response:
                dProgress.total = int(response.headers["Content-Length"])
                dProgress.downloaded = response.num_bytes_downloaded
                dProgress.client = response
                dProgress.started = True
                for chunk in response.iter_bytes():
                    file.write(chunk)
                    dProgress.downloaded += len(chunk)
                    if progress:
                        await progress(dProgress, *progress_args)

        except BaseException as e:
            if not in_memory:
                file.close()
                os.remove(temp_file_path)
            if isinstance(e, CancelError):
                return None
            if isinstance(e, asyncio.CancelledError):
                raise e

            return None
        else:
            if in_memory:
                file.name = file_name
                return file
            else:
                file.close()
                file_path = os.path.splitext(temp_file_path)[0]
                shutil.move(temp_file_path, file_path)
                return file_path

    async def _validate_token(self):
        # check if token is valid
        if self.token is None:
            raise SwitchError("Token is not set")

        try:
            log.debug("checking token...")
            if not self.user:
                user = await self.get_me(user_type=self._user_type)
                self.user = user
            log.info("Logged in as [%s][%d]", self.user.user_name, self.user.id)
        except Exception as e:
            log.exception(e)
            await self.stop()
            raise SwitchError("Invalid token")

        if self.user is None:
            raise SwitchError("Invalid token")

    async def _on_app_stop(self):
        await self.chat_service.stop()
        await self.community_service.stop()
        if self.on_app_stop is not None:
            await self.on_app_stop(self)
        for task in asyncio.all_tasks():
            task.cancel()

    async def _on_app_start(self):
        if self.on_app_start is not None:
            await self.on_app_start(self)

    async def start(self):
        try:
            if self._running:
                return
            self._running = True
            """Starts the app"""
            log.info("🚀 Starting app...")

            await self._validate_token()

            if self.receive_updates:
                try:
                    await self.chat_service.start()
                    if self.on_chat_service_start is not None:
                        await self.on_chat_service_start(self)
                except Exception as e:
                    log.exception(e)

                try:
                    await self.community_service.start()
                    if self.on_community_service_start is not None:
                        await self.on_community_service_start(self)
                except Exception as e:
                    log.exception(e)

            await self._on_app_start()

            log.info("🚀 App started!")

            # # run forever
            # while self._running:
            #     await asyncio.sleep(1)
        except asyncio.CancelledError:
            self._running = False
            # await self._do_stop()

    async def _do_stop(self):
        log.info("🛑 Stopping app...")
        await self._on_app_stop()
        self._running = False

    async def stop(self):
        if not self._running:
            return
        await self._do_stop()

    def __enter__(self):
        return self.start()

    def __exit__(self, *args):
        with suppress(ConnectionError):
            self.stop()

    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self, *args):
        with suppress(ConnectionError):
            await self.stop()

    async def idle(self):
        task = None

        def signal_handler(signum, __):
            logging.info(f"Stop signal received ({signals[signum]}). Exiting...")
            task.cancel()

        for s in (SIGINT, SIGTERM, SIGABRT):
            signal_fn(s, signal_handler)

        while True:
            task = asyncio.create_task(asyncio.sleep(600))

            try:
                await task
            except asyncio.CancelledError:
                break

    def run(self, task: Callable = None):
        loop = asyncio.get_event_loop()
        run = loop.run_until_complete
        if task is not None:
            run(task)
        else:
            try:
                run(self.start())
                run(self.idle())
                run(self.stop())
            except KeyboardInterrupt:
                run(self.stop())
            except Exception as e:
                log.exception(e)
                run(self.stop())


BotApp = Client
