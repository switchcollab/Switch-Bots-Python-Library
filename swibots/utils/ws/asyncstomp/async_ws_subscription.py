from swibots.utils.ws.common import WsMessage


class AsyncWsSubscription:
    def __init__(
        self,
        client,
        destination: str,
        id: str,
        headers: dict[str, str] = None,
        callback=None,
    ):
        from .async_ws_client import AsyncWsClient

        self.client: AsyncWsClient = client
        self.destination = destination
        self.callback = callback
        self.id = id
        self.headers = headers or {}

    async def start(self):
        self.headers["id"] = self.id
        self.headers["destination"] = self.destination
        await self.client._transmit("SUBSCRIBE", self.headers)

    async def receive(self, message):
        if self.callback is not None:
            await self.callback(WsMessage(message))

    async def send(self, body: str, headers: dict[str, str] = None):
        await self.client.send(self.destination, headers or {}, body)

    async def unsubscribe(self):
        await self.client.unsubscribe(self.id)
