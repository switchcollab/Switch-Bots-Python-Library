import asyncio
from contextlib import AbstractContextManager
import logging
import signal
from signal import signal as signal_fn, SIGINT, SIGTERM, SIGABRT
from typing import Callable, Optional
import switch
from switch.api import ApiClient
from switch.api.auth.models import AuthUser
from switch.error import SwitchError

logger = logging.getLogger(f"{__name__}")


log = logging.getLogger(__name__)

# Signal number to name
signals = {
    k: v for v, k in signal.__dict__.items() if v.startswith("SIG") and not v.startswith("SIG_")
}


class App(AbstractContextManager, ApiClient):
    def __init__(
        self,
        token: str,
        loop: asyncio.AbstractEventLoop = None,
    ):
        """Initialize the client"""
        super().__init__()
        self.token = token
        self._loop = loop or asyncio.get_event_loop()
        self._running = False
        self._user_type = AuthUser
        self.on_community_service_start: Callable = None
        self.on_chat_service_start: Callable = None
        self.on_app_stop: Callable = None
        self.on_app_start: Callable = None

    async def _validate_token(self):
        # check if token is valid
        if self.token is None:
            raise SwitchError("Token is not set")

        try:
            logger.debug("checking token...")
            user = await self.get_me(user_type=self._user_type)
            self.user = user
            logger.info("Logged in as %s", user.user_name)
        except Exception as e:
            await self.stop()
            raise SwitchError("Invalid token")

        if self.user is None:
            raise SwitchError("Invalid token")

    async def _validate_run(self):
        await self._validate_token()

    async def _on_app_stop(self):
        await self.chat_service.stop()
        await self.community_service.stop()
        if self.on_app_stop is not None:
            await self.on_app_stop(self)

    async def _on_app_start(self):
        if self.on_app_start is not None:
            await self.on_app_start(self)

    async def start(self):
        try:
            if self._running:
                raise SwitchError("App is already running")
            self._running = True
            """Starts the app"""
            logger.info("🚀 Starting app...")

            await self._validate_run()

            try:
                await (self.chat_service.start())
                if self.on_chat_service_start is not None:
                    await self.on_chat_service_start(self)
            except Exception as e:
                logger.exception(e)

            try:
                await (self.community_service.start())
                if self.on_community_service_start is not None:
                    await self.on_community_service_start(self)
            except Exception as e:
                logger.exception(e)

            await self._on_app_start()

            logger.info("🚀 App started!")

            # # run forever
            # while self._running:
            #     await asyncio.sleep(1)
        except asyncio.CancelledError:
            self._running = False
            # await self._do_stop()

    async def _do_stop(self):
        logger.info("🛑 Stopping app...")
        await self._on_app_stop()
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
                logger.exception(e)
                run(self.stop())