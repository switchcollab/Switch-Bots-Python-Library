import asyncio
import uuid
from typing import List

from swibots.errors import SwitchError

from .async_ws_subscription import AsyncWsSubscription
from swibots.utils.ws.common import WsFrame
from websockets.client import connect
from websockets import exceptions
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
        self._connect_callback = None
        self.error_callback = None
        self._connectIntents = 0
        self._connectInterval = 7
        self._incrementalDelay = 3
        self._maxConnectIntents = 50
        self._connecting = False
        self._gracefully_disconnect = False

    async def _start_heartbeat(self):
        elapsed = 0
        while self.connected:
            await asyncio.sleep(0.1)
            elapsed = elapsed + 0.1
            if elapsed >= 5:
                await self.transmit("\n", {})
                elapsed = 0
        log.debug("Heartbeat stopped")

    async def _on_open(self, ws_app, *args):
        self.opened = True

    async def _on_close(self, ws_app, *args):
        self.connected = False
        if self._gracefully_disconnect:
            return
        log.error("Whoops! Lost connection to " + self.url)
        await self._clean_up()
        if self._connectIntents >= self._maxConnectIntents > 0:
            log.error("Max connection attempts reached. Aborting.")
            raise SwitchError("Max connection attempts reached. Aborting.")
        wait_time = self._connectInterval
        if self._connectIntents:
            wait_time += self._connectIntents * self._incrementalDelay
        log.info(f"Waiting for {wait_time}s before retry!")
        await asyncio.sleep(wait_time)
        self._connectIntents += 1
        await self.connect(**self._connect_args)

    async def _on_error(self, ws_app, error, *args):
        await self._clean_up()
        await self._on_close(ws_app, *args)
        if error:
            log.error(error)

    async def _on_message(self, ws_app, message, *args):
        frame = WsFrame.unmarshall_single(message)

        if frame.command != "PONG":
            log.debug("\n<<< " + str(message))
        else:
            log.debug("\n<<< " + frame.command)

        _results = []
        if frame.command == "CONNECTED":
            if self._connectIntents:
                log.info("connected to server " + self.url)
            self.connected = True
            self._connecting = False
            self._connectIntents = 0
            self._heartbeatTask = self._loop.create_task(self._start_heartbeat())
            # resubscribe
            for sub in self.subscriptions.values():
                await self._start_subscription(sub)

            # if self._connect_callback is not None:
            #     _results.append(await self._send_heartbeat(frame))
        elif frame.command == "MESSAGE":
            subscription = frame.headers["subscription"]

            if subscription in self.subscriptions:
                sub = self.subscriptions[subscription]
                message_id = frame.headers["message-id"]

                async def ack(headers):
                    if headers is None:
                        headers = {}
                    return await self.ack(message_id, subscription, headers)

                async def nack(headers):
                    if headers is None:
                        headers = {}
                    return await self.nack(message_id, subscription, headers)

                frame.ack = ack
                frame.nack = nack

                _results.append(self._loop.create_task(sub.receive(frame)))
            else:
                info = "Unhandled received MESSAGE: " + str(frame)
                log.debug(info)
                _results.append(info)
        elif frame.command == "ERROR":
            if self.error_callback is not None:
                _results.append(self.error_callback(frame))
        elif frame.command not in ["PONG", "RECEIPT"]:
            info = "Unhandled received MESSAGE: " + frame.command
            log.debug(info)
            _results.append(info)

        return _results

    async def transmit(self, command, headers, body=None):
        try:
            if self.ws is None:
                return
            out = WsFrame.marshall(command, headers, body)
            if command == "\n":
                out = command
            log.debug("\n>>> {}".format("PING" if command == "\n" else out))
            await self.ws.send(out)
        except exceptions.WebSocketException as er:
            log.error(er)
            await self._on_close(self.ws)
        except Exception as e:
            await self._on_error(self.ws, e)

    async def connect(
        self,
        login=None,
        passcode=None,
        headers=None,
        connect_callback=None,
        error_callback=None,
        timeout=0,
        **kwargs,
    ):
        headers = self._set_default_headers(headers)
        await self._connect(login, passcode, headers,
                            connect_callback, error_callback,
                            timeout, **kwargs)

    async def _connect(
        self,
        login=None,
        passcode=None,
        headers=None,
        connect_callback=None,
        error_callback=None,
        timeout=30,
        **kwargs,
    ):
        if self.connected:
            log.debug("Already connected to " + self.url)
            return

        if self._connecting:
            log.debug("Already connecting to " + self.url)
            return

        try:
            self._connecting = True
            self._connect_args = kwargs
            log.debug("Opening web socket...")
            self.ws = await connect(self.url)
            log.debug("Web socket opened.")
            self._loop.create_task(self.read_messages())
            headers = headers if headers is not None else {}
            # headers['host'] = self.url
            headers["accept-version"] = VERSIONS
            headers["heart-beat"] = "10000,10000"
            if login is not None:
                headers["login"] = login
            if passcode is not None:
                headers["passcode"] = passcode
            self._connect_callback = connect_callback
            self.error_callback = error_callback
            await self.transmit("CONNECT", headers)
            # elapsed time
            elapsed = 0
            while not self.connected:
                await asyncio.sleep(1)
                elapsed += 1
                if 0 < timeout < elapsed:
                    raise Exception("Connection timeout")
        except (exceptions.WebSocketException,):
            await self._on_close(self.ws)
        except Exception as e:
            await self._on_error(self.ws, e)

    async def read_messages(self):
        try:
            async for message in self.ws:
                await self._on_message(self.ws, message)
            await self._on_close(self.ws)
        except exceptions.WebSocketException as er:
            log.error(er)
            await self._on_close(self.ws)
        except Exception as e:
            await self._on_error(self.ws, e)

    async def disconnect(self, disconnect_callback=None, headers=None):
        headers = self._set_default_headers(headers)
        await self.transmit("DISCONNECT", headers)
        self._gracefully_disconnect = True
        await self.ws.close()
        await self._clean_up()
        if disconnect_callback is not None:
            disconnect_callback()

    async def _clean_up(self):
        try:
            self.connected = False
            self._connecting = False
            self.opened = False
            self.tasks = []
        except Exception as e:
            log.debug("Error cleaning up: " + str(e))

    async def send(self, destination, headers=None, body=None):
        headers = self._set_default_headers(headers)
        if body is None:
            body = ""
        headers["destination"] = destination
        return await self.transmit("SEND", headers, body)

    async def subscribe(self, destination, callback=None, headers=None):
        headers = self._set_default_headers(headers)
        sub_id = f"sub-{uuid.uuid4()}"
        headers["id"] = sub_id

        sub = AsyncWsSubscription(
            client=self,
            destination=destination,
            callback=callback,
            headers=headers,
            sub_id=sub_id,
        )
        await self._start_subscription(sub)
        self.subscriptions[sub_id] = sub
        return sub

    def _set_default_headers(self, headers):
        return headers or {}

    @staticmethod
    async def _start_subscription(subscription: AsyncWsSubscription):
        return await subscription.start()

    async def unsubscribe(self, sub_id):
        del self.subscriptions[sub_id]
        return await self.transmit("UNSUBSCRIBE", {"id": sub_id})

    async def ack(self, message_id, subscription, headers):
        headers = self._set_default_headers(headers)
        headers["message-id"] = message_id
        headers["subscription"] = subscription
        return await self.transmit("ACK", headers)

    async def nack(self, message_id, subscription, headers):
        headers = self._set_default_headers(headers)
        headers["message-id"] = message_id
        headers["subscription"] = subscription
        return await self.transmit("NACK", headers)
