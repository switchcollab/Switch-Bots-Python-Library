from swibots.utils.ws.common import WsMessage


class WsSubscription:
    def __init__(
        self, client, destination: str, id: str, headers: dict[str, str] = None, callback=None
    ):
        from .ws_client import WsClient

        self.client: WsClient = client
        self.destination = destination
        self.callback = callback
        self.id = id
        self.headers = headers or {}

    def start(self):
        self.headers["id"] = self.id
        self.headers["destination"] = self.destination
        self.client._transmit("SUBSCRIBE", self.headers)

    def receive(self, message):
        if self.callback is not None:
            self.callback(WsMessage(message))

    def send(self, body: str, headers: dict[str, str] = None):
        headers = headers or {}
        self.client.send(self.destination, headers, body)

    def unsubscribe(self):
        self.client.unsubscribe(self.id)
