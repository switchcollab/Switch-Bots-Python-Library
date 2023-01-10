import asyncio
import logging
from switch.api.switch_client import SwitchClient
from switch.bots import BaseHandler
from switch.error import SwitchError

logger = logging.getLogger(__name__)

class SwitchApp:
    def __init__(self):
        self._switch_client: SwitchClient = None
    
    @property
    def api(self) -> SwitchClient:
        if self._switch_client is None:
            self._switch_client = SwitchClient()
        return self._switch_client

    def token(self, value: str) -> 'SwitchApp': 
        self.api.token = value
        return self

    def build(self):
        self.api.initialize()


    def add_handler(self, handler: BaseHandler):
        pass

    async def _validate_token(self):
         # check if token is valid
        if self.api.token is None:
            raise SwitchError("Token is not set")
        
        try:
            logger.debug("checking token...")
            user=await self.api.auth.users.me()
            self.api.user = user
            logger.debug("token is valid %s", user)
        except Exception as e:
            await self.stop()
            raise SwitchError("Invalid token")

        if self.api.user is None or not self.api.user.is_bot:
            raise SwitchError("Invalid token (not a bot token)")

    async def _validate_run(self):
       await self._validate_token()

    async def on_message(self, message):
        print(message)

    async def run(self):
        """Starts the app"""
        await self._validate_run()
        await self.api.chat.ws.connect()
        await self.api.chat.ws.subscribe("/topic/listen.277", callback=self.on_message)
        await self.api.chat.ws.send("/topic/listen.277", {}, "hello")
        while True:
            await asyncio.sleep(1)
    
    async def stop(self):
        """Stops the app"""
        print("app stopped")

    @staticmethod
    def builder() -> 'SwitchAppBuilder':
        return SwitchAppBuilder()
        

class SwitchAppBuilder:
    def __init__(self):
        self._switch_app: SwitchApp = SwitchApp()
    
    def token(self, value: str) -> 'SwitchAppBuilder':
        self._switch_app.token(value)
        return self

    def build(self) -> SwitchApp:
        self._switch_app.build()
        return self._switch_app
       
