from typing import Dict
from swibots.utils.ws.common import WsMessage


class AsyncWsSubscription:
    def __init__(
        self,
        client,
        destination: str,
        sub_id: str,
        headers: Dict[str, str] = None,
        callback=None,
    ):
        from .async_ws_client import AsyncWsClient

        self.client: AsyncWsClient = client
        self.destination = destination
        self.callback = callback
        self.sub_id = sub_id
        self.headers = headers or {}

    async def start(self):
        self.headers["id"] = self.sub_id
        self.headers["destination"] = self.destination
        await self.client.transmit("SUBSCRIBE", self.headers)

    async def receive(self, message):
        if self.callback is not None:
            await self.callback(WsMessage(message))

    async def send(self, body: str, headers: Dict[str, str] = None):
        await self.client.send(self.destination, headers or {}, body)

    async def unsubscribe(self):
        await self.client.unsubscribe(self.sub_id)
