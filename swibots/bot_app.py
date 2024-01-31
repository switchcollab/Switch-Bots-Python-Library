import re, httpx
import os, signal
import asyncio
import logging
import shutil
from contextlib import AbstractContextManager
from typing import List, Optional, Callable
import swibots
from contextlib import suppress
from pathlib import Path
from signal import signal as signal_fn, SIGINT, SIGTERM, SIGABRT
from io import BytesIO
from swibots.bots import Bot
from importlib import import_module
from swibots.errors import SwitchError, CancelError
from swibots.api.community.events import CommunityEvent
from swibots.api.chat.events import ChatEvent
from swibots.bots import BotContext, Decorators, BaseHandler
from swibots.api.bot.models import BotInfo, BotCommand
from swibots.api.callback import AppBar
from swibots.api.common.events import Event
from swibots.utils import (
    DownloadProgress,
    IOClient,
    RestClient,
    DownloadProgressCallback,
)
from swibots.errors import TokenInvalidError
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
        plugins: dict = None,
        auto_update_bot: Optional[bool] = True,
        loop: asyncio.AbstractEventLoop = None,
        receive_updates: Optional[bool] = True,
        app_bar: Optional[AppBar] = AppBar(),
    ):
        """
        Initialize the client

        Args:
            token (:obj:`str`): The bot token.
            bot_description(:obj:`str`): The bot description.
            auto_update_bot(:obj:`bool`): Whether to automatically update the bot description and the registered commands.
            plugins(:obj:`dict`): plugin path to load, use as: dict(root="plugins")
            loop (:obj:`asyncio.AbstractEventLoop`): The asyncio loop to use (default: asyncio.get_event_loop()).

        """
        super().__init__()
        self.token = token
        if not token:
            raise TokenInvalidError(f"'token' for the bot can't be '{token}'")
        self._user_type = Bot
        self._bot_info: BotInfo | None = None
        self.on_app_start = None
        self.on_app_stop = None
        self.on_chat_service_start = self._on_chat_service_start
        self.on_community_service_start = self._on_community_service_start
        self._handlers: List[BaseHandler] = []
        self._register_commands: List[BotCommand] = []
        self._bot_description = bot_description
        self.auto_update_bot = auto_update_bot
        self._loop = loop or asyncio.get_event_loop()
        self.user = self.auth_service.get_me_sync(user_type=self._user_type)
        self.name = self.user.name
        self._bot_id = None
        self._running = False
        self._user_type = Bot
        self.rest_client = RestClient()
        self.receive_updates = receive_updates
        self.plugins = plugins or dict()
        self.app_bar = app_bar

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
        return self._handlers

    def load_path(self, path):
        base_name = os.path.basename(path)
        if base_name.startswith("__") or not base_name.endswith(".py"):
            return
        try:
            module_path = path[:-3].replace("\\", ".").replace("/", ".")

            return import_module(module_path)
        except Exception as er:
            LoaderLog.exception(er)

    def load_plugins(self):
        if not self.plugins:
            return
        plugins = self.plugins.copy()

        for option in ["include", "exclude"]:
            if plugins.get(option, []):
                plugins[option] = [
                    (i.split()[0], i.split()[1:] or None) for i in self.plugins[option]
                ]

        root = plugins["root"]
        include = plugins.get("include", [])
        exclude = plugins.get("exclude", [])

        count = 0

        if not include:
            for path in sorted(Path(root.replace(".", "/")).rglob("*.py")):
                module_path = ".".join(path.parent.parts + (path.stem,))
                try:
                    module = import_module(module_path)
                    count += 1
                except Exception as er:
                    log.exception(er)
        else:
            for path in include:
                module_path = root + "." + path

                try:
                    module = import_module(module_path)
                    count += 1
                except ImportError:
                    continue

                if "__path__" in dir(module):
                    continue

        if exclude:
            for path in exclude:
                module_path = root + "." + path

                try:
                    module = import_module(module_path)
                except ImportError:
                    continue

                if "__path__" in dir(module):
                    continue

        if count > 0:
            log.info(
                '[{}] Successfully loaded {} modules{} from "{}"'.format(
                    self.name, count, "s" if count > 1 else "", root
                )
            )
            return
        log.warning('[%s] No modules loaded from "%s"', self.name, root)

    def set_bot_commands(self, command: BotCommand | List[BotCommand]) -> "BotApp":
        if isinstance(command, list):
            self._register_commands.extend(command)
        else:
            self._register_commands.append(command)
        asyncio.run_coroutine_threadsafe(self.update_bot_commands(), self._loop)
        return self

    def delete_bot_commands(self, command: BotCommand | List[BotCommand]) -> "Client":
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
        self._bot_info = BotInfo(
            description=description,
            id=self._bot_id,
            commands=commands,
        )

        self._bot_info = await self.update_bot_info(self._botinfo)

    async def _on_chat_service_start(self, _):
        await self.chat_service.subscribe_to_notifications(
            callback=self.on_chat_event
        )

    async def _on_community_service_start(self, _):
        await self.community_service.subscribe_to_notifications(
            callback=self.on_community_event
        )

    def _build_context(self, event: Event) -> BotContext:
        return BotContext(app=self, event=event)

    async def process_event(self, ctx: BotContext):
        for handler in self.handlers:
            try:
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

        d_progress = DownloadProgress(
            total=0,
            downloaded=0,
            file_name=file_name,
            client=IOClient(),
            url=url,
        )

        if progress:
            await progress(d_progress, *progress_args)
        try:
            with httpx.stream("GET", url) as response:
                d_progress.total = int(response.headers["Content-Length"])
                d_progress.downloaded = response.num_bytes_downloaded
                d_progress.client = response
                d_progress.started = True
                for chunk in response.iter_bytes():
                    file.write(chunk)
                    d_progress.downloaded += len(chunk)
                    if progress:
                        await progress(d_progress, *progress_args)

        except BaseException as e:
            if not in_memory:
                file.close()
                os.remove(temp_file_path)
            if isinstance(e, CancelError):
                return None
            if isinstance(e, asyncio.CancelledError):
                raise e
            raise e
        if in_memory:
            file.name = file_name
            return file
        else:
            file.close()
            file_path = os.path.splitext(temp_file_path)[0]
            shutil.move(temp_file_path, file_path)
            return file_path

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

            log.info(
                "Logged in as [%a][%s][%d]",
                self.user.name,
                self.user.user_name,
                self.user.id,
            )
            self.name = self.user.user_name
            self._bot_id = self.user.id

            self.load_plugins()

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

        except asyncio.CancelledError:
            self._running = False

    async def stop(self):
        if not self._running:
            return
        log.info("🛑 Stopping app...")
        await self._on_app_stop()
        self._running = False

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
            return run(task)
        else:
            try:
                run(self.start())
                run(self.idle())
                run(self.stop())
            except KeyboardInterrupt:
                run(self.stop())
            except asyncio.exceptions.CancelledError as er:
                log.debug(er)
            except Exception as e:
                log.exception(e)
                run(self.stop())


BotApp = Client
