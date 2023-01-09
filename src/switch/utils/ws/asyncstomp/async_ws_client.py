import asyncio

from .async_ws_subscription import AsyncWsSubscription
from switch.utils.ws.common import WsFrame
import websockets
import logging

VERSIONS = '1.1,1.0'


class AsyncWsClient:

    def __init__(self, url: str, ):

        self.url = url
        self.ws = websockets.connect(self.url)
        self._loop = asyncio.get_event_loop()
        self.opened = False
        self.connected = False
        self.counter = 0
        self.subscriptions: dict[str, AsyncWsSubscription] = {}
        self._connect_args = None
        self._connectCallback = None
        self.errorCallback = None

        self._heartbeat_thread = None

    async def _send_heartbeat(self):
        while True:
            await asyncio.sleep(5)
            await self._transmit("\n", {})

    async def _start_heartbeat(self):
        await self._send_heartbeat()

    def _on_open(self, ws_app, *args):
        self.opened = True

    def _on_close(self, ws_app, *args):
        self.connected = False
        logging.debug("Whoops! Lost connection to " + self.ws.url)
        self._clean_up()
        self.connect(**self._connect_args)

    def _on_error(self, ws_app, error, *args):
        logging.debug(error)

    async def _on_message(self, ws_app, message, *args):
        frame = WsFrame.unmarshall_single(message)

        if frame.command != "PONG":
            logging.debug("\n<<< " + str(message))
        else:
            logging.debug("\n<<< " + frame.command)

        _results = []
        if frame.command == "CONNECTED":
            self.connected = True
            logging.debug("connected to server " + self.url)
            self._loop.create_task(self._start_heartbeat())
            # if self._connectCallback is not None:
            #     _results.append(await self._send_heartbeat(frame))
        elif frame.command == "MESSAGE":

            subscription = frame.headers['subscription']

            if subscription in self.subscriptions:
                sub = self.subscriptions[subscription]
                messageID = frame.headers['message-id']

                async def ack(headers):
                    if headers is None:
                        headers = {}
                    return await self.ack(messageID, subscription, headers)

                async def nack(headers):
                    if headers is None:
                        headers = {}
                    return await self.nack(messageID, subscription, headers)

                frame.ack = ack
                frame.nack = nack

                _results.append(self._loop.create_task(sub.receive(frame)))
            else:
                info = "Unhandled received MESSAGE: " + str(frame)
                logging.debug(info)
                _results.append(info)
        elif frame.command == 'RECEIPT':
            pass
        elif frame.command == 'ERROR':
            if self.errorCallback is not None:
                _results.append(self.errorCallback(frame))
        elif frame.command == 'PONG':
            pass
        else:
            info = "Unhandled received MESSAGE: " + frame.command
            logging.debug(info)
            _results.append(info)

        return _results

    async def _transmit(self, command, headers, body=None):
        out = l = WsFrame.marshall(command, headers, body)
        if command == "\n":
            l = "PING"
            out = command
        logging.debug("\n>>> " + l)
        await self.ws.send(out)

    async def connect(self, login=None, passcode=None, headers=None, connectCallback=None, errorCallback=None,
                      timeout=0, **kwargs):
        await self._connect(login, passcode, headers,
                            connectCallback, errorCallback, timeout, **kwargs)

    async def _connect(self, login=None, passcode=None, headers=None, connectCallback=None, errorCallback=None,
                       timeout=0, **kwargs):

        self._connect_args = kwargs
        logging.debug("Opening web socket...")
        self.ws = await websockets.connect(self.url)
        logging.debug("Web socket opened.")
        self._loop.create_task(self.read_messages())
        headers = headers if headers is not None else {}
        # headers['host'] = self.url
        headers['accept-version'] = VERSIONS
        headers['heart-beat'] = '10000,10000'
        if login is not None:
            headers['login'] = login
        if passcode is not None:
            headers['passcode'] = passcode
        self._connectCallback = connectCallback
        self.errorCallback = errorCallback
        await self._transmit('CONNECT', headers)
        # await self._start_heartbeat()

    async def read_messages(self):
        async for message in self.ws:
            await self._on_message(self.ws, message)

    async def disconnect(self, disconnectCallback=None, headers=None):
        if headers is None:
            headers = {}
        self._clean_up()
        await self._transmit("DISCONNECT", headers)
        if disconnectCallback is not None:
            disconnectCallback()

    def _clean_up(self):
        self.connected = False
        self.opened = False

    async def send(self, destination, headers=None, body=None):
        if headers is None:
            headers = {}
        if body is None:
            body = ''
        headers['destination'] = destination
        return await self._transmit("SEND", headers, body)

    async def subscribe(self, destination, callback=None, headers=None):
        if headers is None:
            headers = {}
        if 'id' not in headers or headers['id'] is None or headers['id'] == "":
            id = "sub-" + str(self.counter)
            self.counter += 1
        else:
            id = headers['id']

        sub = AsyncWsSubscription(client=self, destination=destination,
                                  callback=callback, headers=headers, id=id)
        await self._start_subscription(sub)
        self.subscriptions[id] = sub
        return sub

    async def _start_subscription(self, subscription: AsyncWsSubscription):
        return await subscription.start()

    async def unsubscribe(self, id):
        del self.subscriptions[id]
        return await self._transmit("UNSUBSCRIBE", {
            "id": id
        })

    async def ack(self, message_id, subscription, headers):
        if headers is None:
            headers = {}
        headers["message-id"] = message_id
        headers['subscription'] = subscription
        return await self._transmit("ACK", headers)

    async def nack(self, message_id, subscription, headers):
        if headers is None:
            headers = {}
        headers["message-id"] = message_id
        headers['subscription'] = subscription
        return await self._transmit("NACK", headers)
