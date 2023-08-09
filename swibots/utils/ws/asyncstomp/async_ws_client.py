import asyncio
from typing import List

from swibots.error import SwitchError

from .async_ws_subscription import AsyncWsSubscription
from concurrent.futures.thread import ThreadPoolExecutor
from swibots.utils.ws.common import WsFrame
from websocket import (
    create_connection,
    WebSocket,
    WebSocketApp,
    WebSocketConnectionClosedException,
    WebSocketException,
    enableTrace,
)
import logging

VERSIONS = "1.1,1.0"

log = logging.getLogger(__name__)


class AsyncWsClient:
    def __init__(
        self,
        url: str,
    ):
        self.url = url
        self.ws = None
        self._loop = asyncio.get_event_loop()
        self.opened = False
        self.connected = False
        self.counter = 0
        self.tasks: List[asyncio.Task] = []
        self._heartbeatTask = None
        self.subscriptions: dict[str, AsyncWsSubscription] = {}
        self._connect_args = {}
        self._connectCallback = None
        self.errorCallback = None
        self._connectIntents = 0
        self._connectInterval = 1
        self._maxConnectIntents = 0
        self.executor = ThreadPoolExecutor(10)
        self._connecting = False
        self._gracefully_disconnect = False

    async def _start_heartbeat(self):
        elapsed = 0
        while self.connected:
            await asyncio.sleep(0.1)
            elapsed += 0.1
            if elapsed >= 5:
                await self._transmit("\n", {})
                elapsed = 0
        log.debug("Heartbeat stopped")

    async def _on_close(self, ws_app, *args):
        self.connected = False
        self._connecting = False
        if self._gracefully_disconnect:
            return
        log.error("Whoops! Lost connection to " + self.url)
        await self._clean_up()
        if (
            self._maxConnectIntents > 0
            and self._connectIntents >= self._maxConnectIntents
        ):
            log.error("Max connection attempts reached. Aborting.")
            raise SwitchError("Max connection attempts reached. Aborting.")
        await asyncio.sleep(self._connectInterval)
        self._connectIntents += 1
        await self.connect(**self._connect_args)

    async def _on_error(self, ws_app, error, *args):
        log.exception(error)
        await self._clean_up()
        await self._on_close(ws_app, *args)

    async def _on_message(self, message, *args):
        frame = WsFrame.unmarshall_single(message)
        if frame.command != "PONG":
            log.debug("\n<<< " + str(message))
        else:
            log.debug("\n<<< " + frame.command)
        _results = []
        if frame.command == "CONNECTED":
            self.connected = True
            self._connecting = False

            if self._connectIntents > 0:
                log.info("Re-Established connection to the server " + self.url)
            else:
                log.info("connected to server " + self.url)

            self._connectIntents = 0
            # resubscribe
            for sub in self.subscriptions.values():
                await self._start_subscription(sub)

            # if self._connectCallback is not None:
            #     _results.append(await self._send_heartbeat(frame))
        elif frame.command == "MESSAGE":
            subscription = frame.headers["subscription"]

            if subscription in self.subscriptions:
                sub = self.subscriptions[subscription]
                messageID = frame.headers["message-id"]

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

                _results.append(
                    # self._loop.create_task(sub.receive(frame))
                    self._loop.run_in_executor(
                        self.executor,
                        lambda: asyncio.new_event_loop().run_until_complete(
                            sub.receive(frame)
                        ),
                    )
                )
            else:
                info = "Unhandled received MESSAGE: " + str(frame)
                log.debug(info)
                _results.append(info)
        elif frame.command == "ERROR":
            if self.errorCallback is not None:
                _results.append(self.errorCallback(frame))
        elif frame.command not in ["PONG", "RECEIPT"]:
            info = "Unhandled received MESSAGE: " + frame.command
            log.debug(info)
            _results.append(info)

        return _results

    async def _transmit(self, command, headers, body=None):
        try:
            out = l = WsFrame.marshall(command, headers, body)
            if command == "\n":
                l = "PING"
                out = command
            log.debug("\n>>> " + l)
            self.ws.send(out)
        except WebSocketConnectionClosedException as er:
            if "socket is already closed.":
                self.connected = False
                self._gracefully_disconnect = True
                await self._on_close(self.ws)
                return
            raise er
        except OSError:
            return
        except Exception as e:
            log.exception(e)
            await self._on_error(self.ws, e)

    async def connect(
        self,
        login=None,
        passcode=None,
        headers=None,
        connectCallback=None,
        errorCallback=None,
        timeout=0,
        **kwargs,
    ):
        headers = self._set_default_headers(headers)
        await self._connect(
            login, passcode, headers, connectCallback, errorCallback, timeout, **kwargs
        )

    async def _connect(
        self,
        login=None,
        passcode=None,
        headers=None,
        connectCallback=None,
        errorCallback=None,
        timeout=30,
        **kwargs,
    ):
        if self.connected:
            log.error("Already connected to " + self.url)
            return

        if self._connecting:
            log.error("Already connecting to " + self.url)
            return

        try:
            self._connecting = True
            self._connect_args = kwargs
            log.debug("Opening web socket...")
            headers = headers if headers is not None else {}

            headers["accept-version"] = VERSIONS
            headers["heart-beat"] = "10000,10000"
            if login is not None:
                headers["login"] = login
            if passcode is not None:
                headers["passcode"] = passcode
            self._connectCallback = connectCallback
            self.errorCallback = errorCallback

            await self.getWebsocket(headers)
            #            self.ws.connect(self.url, header=headers, timeout=120)
            #            await self._transmit("CONNECT", headers)
            self._loop.run_in_executor(
                self.executor,
                lambda: asyncio.new_event_loop().run_until_complete(
                    self.read_messages(headers)
                ),
            )
            #          Thread(target=self.ws.run_forever).start()

            # self.read_messages(headers))
            # headers['host'] = self.url

            # elapsed time
            elapsed = 0
            while not (self.ws):
                await asyncio.sleep(0.5)
                elapsed += 0.5
                if timeout > 0 and elapsed > timeout:
                    raise Exception("Connection timeout")
            if self._connectIntents > 0:
                log.info(f"Retrying connection to {self.url}")
        # await self._start_heartbeat()

        except Exception as e:
            log.exception(e)
            await self._on_error(self.ws, e)

    async def getWebsocket(self, headers):
        if self.ws:
            return self.ws
        self.ws = create_connection(self.url, header=headers, timeout=420)
        await self._transmit("CONNECT", headers)
        return self.ws

    async def read_messages(self, headers):
        try:
            await self.getWebsocket(headers)

            while self.ws.connected:
                message = self.ws.recv()
                await self._on_message(message)
                await self._transmit("\n", headers)
        except Exception as e:
            log.exception(e)
            await self._on_error(self.ws, e)
            return
        await self._on_close(self.ws)

    async def disconnect(self, disconnectCallback=None, headers=None):
        headers = self._set_default_headers(headers)
        await self._transmit("DISCONNECT", headers)
        self._gracefully_disconnect = True
        if self.ws:
            self.ws.close()
        await self._clean_up()
        if disconnectCallback is not None:
            disconnectCallback()

    async def _clean_up(self):
        try:
            self.connected = False
            self._connecting = False
            self.opened = False
            if self._heartbeatTask:
                self._heartbeatTask.cancel()
                self._heartbeatTask = None

            # if self._heartbeatTask is not None:
            #     await asyncio.wait_for(self._heartbeatTask, 5)
            # [task.cancel() for task in self.tasks]
            # self.ws = None
            self.tasks = []
            for id in list(self.subscriptions.keys()):
                try:
                    await self.subscriptions[id].unsubscribe()
                except KeyError:
                    pass
        except Exception as e:
            log.exception(e)
            log.debug("Error cleaning up: " + str(e))

    async def send(self, destination, headers=None, body=None):
        headers = self._set_default_headers(headers)
        if body is None:
            body = ""
        headers["destination"] = destination
        return await self._transmit("SEND", headers, body)

    async def subscribe(self, destination, callback=None, headers=None):
        headers = self._set_default_headers(headers)
        if "id" not in headers or headers["id"] is None or headers["id"] == "":
            id = "sub-" + str(self.counter)
            self.counter += 1
        else:
            id = headers["id"]

        sub = AsyncWsSubscription(
            client=self,
            destination=destination,
            callback=callback,
            headers=headers,
            id=id,
        )
        await sub.start()
        #        await sub.start()
        #        await self._start_subscription(sub)
        self.subscriptions[id] = sub
        return sub

    def _set_default_headers(self, headers):
        return headers or {}

    async def _start_subscription(self, subscription: AsyncWsSubscription):
        return await subscription.start()

    async def unsubscribe(self, id):
        del self.subscriptions[id]
        return await self._transmit("UNSUBSCRIBE", {"id": id})

    async def ack(self, message_id, subscription, headers):
        headers = self._set_default_headers(headers)
        headers["message-id"] = message_id
        headers["subscription"] = subscription
        return await self._transmit("ACK", headers)

    async def nack(self, message_id, subscription, headers):
        headers = self._set_default_headers(headers)
        headers["message-id"] = message_id
        headers["subscription"] = subscription
        return await self._transmit("NACK", headers)
