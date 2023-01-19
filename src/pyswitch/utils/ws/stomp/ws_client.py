import time
from threading import Thread

from pyswitch.utils.ws.common import WsFrame
from .ws_subscription import WsSubscription
import websocket
import logging

VERSIONS = "1.1,1.0"


class WsClient:
    def __init__(self, url: str):

        self.url = url
        self.ws = websocket.WebSocketApp(self.url)
        self.ws.on_open = self._on_open
        self.ws.on_message = self._on_message
        self.ws.on_error = self._on_error
        self.ws.on_close = self._on_close

        self.opened = False

        self.connected = False

        self.counter = 0
        self.subscriptions: dict[str, WsSubscription] = {}

        self._connect_args = None

        self._connectCallback = None
        self.errorCallback = None

        self._heartbeat_thread = None

    def _connect(self, timeout=0):
        thread = Thread(target=self.ws.run_forever)
        thread.daemon = True
        thread.start()
        total_ms = 0
        while self.opened is False:
            time.sleep(0.25)
            total_ms += 250
            if 0 < timeout < total_ms:
                raise TimeoutError(f"Connection to {self.url} timed out")

    def _do_heartbeat(self):
        while self.connected:
            time.sleep(5)
            self._transmit("\n", {})

    def start_heartbeat(self):
        self._heartbeat_thread = Thread(target=self._do_heartbeat)
        self._heartbeat_thread.daemon = True
        self._heartbeat_thread.start()

    def _on_open(self, ws_app, *args):
        self.opened = True

    def _on_close(self, ws_app, *args):
        self.connected = False
        logging.debug("Whoops! Lost connection to " + self.ws.url)
        self._clean_up()
        self.connect(**self._connect_args)

    def _on_error(self, ws_app, error, *args):
        logging.debug(error)

    def _on_message(self, ws_app, message, *args):
        frame = WsFrame.unmarshall_single(message)

        if frame.command != "PONG":
            logging.debug("\n<<< " + str(message))
        else:
            logging.debug("\n<<< " + frame.command)

        _results = []
        if frame.command == "CONNECTED":
            self.connected = True
            logging.debug("connected to server " + self.url)
            self.start_heartbeat()
            if self._connectCallback is not None:
                _results.append(self._connectCallback(frame))
        elif frame.command == "MESSAGE":

            subscription = frame.headers["subscription"]

            if subscription in self.subscriptions:
                sub = self.subscriptions[subscription]
                messageID = frame.headers["message-id"]

                async def ack(headers):
                    if headers is None:
                        headers = {}
                    return self.ack(messageID, subscription, headers)

                async def nack(headers):
                    if headers is None:
                        headers = {}
                    return self.nack(messageID, subscription, headers)

                frame.ack = ack
                frame.nack = nack

                _results.append(sub.receive(frame))
            else:
                info = "Unhandled received MESSAGE: " + str(frame)
                logging.debug(info)
                _results.append(info)
        elif frame.command == "RECEIPT":
            pass
        elif frame.command == "ERROR":
            if self.errorCallback is not None:
                _results.append(self.errorCallback(frame))
        elif frame.command == "PONG":
            pass
        else:
            info = "Unhandled received MESSAGE: " + frame.command
            logging.debug(info)
            _results.append(info)

        return _results

    def _transmit(self, command, headers, body=None):
        out = l = WsFrame.marshall(command, headers, body)
        if command == "\n":
            l = "PING"
            out = command
        logging.debug("\n>>> " + l)
        self.ws.send(out)

    def connect(
        self,
        login=None,
        passcode=None,
        headers=None,
        connectCallback=None,
        errorCallback=None,
        timeout=0,
        **kwargs,
    ):

        self._connect_args = kwargs

        logging.debug("Opening web socket...")
        self._connect(timeout)

        headers = headers if headers is not None else {}
        # headers['host'] = self.url
        headers["accept-version"] = VERSIONS
        headers["heart-beat"] = "10000,10000"

        if login is not None:
            headers["login"] = login
        if passcode is not None:
            headers["passcode"] = passcode

        self._connectCallback = connectCallback
        self.errorCallback = errorCallback

        self._transmit("CONNECT", headers)

    def disconnect(self, disconnectCallback=None, headers=None):
        if headers is None:
            headers = {}
        self._clean_up()
        self._transmit("DISCONNECT", headers)
        self.ws.on_close = None
        self.ws.close()

        if disconnectCallback is not None:
            disconnectCallback()

    def _clean_up(self):
        self.connected = False
        self.opened = False

    def send(self, destination, headers=None, body=None):
        if headers is None:
            headers = {}
        if body is None:
            body = ""
        headers["destination"] = destination
        return self._transmit("SEND", headers, body)

    def subscribe(self, destination, callback=None, headers=None):
        if headers is None:
            headers = {}
        if "id" not in headers or headers["id"] is None or headers["id"] == "":
            id = "sub-" + str(self.counter)
            self.counter += 1
        else:
            id = headers["id"]

        sub = WsSubscription(
            client=self, destination=destination, callback=callback, headers=headers, id=id
        )
        self._start_subscription(sub)
        self.subscriptions[id] = sub
        return sub

    def _start_subscription(self, subscription: WsSubscription):
        return subscription.start()

    def unsubscribe(self, id):
        del self.subscriptions[id]
        return self._transmit("UNSUBSCRIBE", {"id": id})

    def ack(self, message_id, subscription, headers):
        if headers is None:
            headers = {}
        headers["message-id"] = message_id
        headers["subscription"] = subscription
        return self._transmit("ACK", headers)

    def nack(self, message_id, subscription, headers):
        if headers is None:
            headers = {}
        headers["message-id"] = message_id
        headers["subscription"] = subscription
        return self._transmit("NACK", headers)
