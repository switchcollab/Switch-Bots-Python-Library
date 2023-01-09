import asyncio
import logging
import os
from pathlib import Path
import sys
from websockets import connect

TOKEN = os.getenv("ACCESS_TOKEN") if os.getenv("ACCESS_TOKEN") else ""
uri = "ws://51.158.56.0:8080/comm"
logging.basicConfig(level=logging.DEBUG)


async def on_message(frame, message):
    print(message)
    return True


async def report_error(error):
    print("report_error", error)


async def hello(uri):
    async with connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()


async def run():
    headers = {"Authorization": "Bearer " + TOKEN}

    # websocket.enableTrace(True)
    # ws = websocket.WebSocketApp(uri, header=headers, on_message=on_msg)
    # ws.on_open = on_open
    # ws.run_forever()
    client = AsyncWsClient(uri)

    # connect to the endpoint
    await client.connect(headers={**headers})
    await client.subscribe("/topic/messages", headers={**headers}, callback=on_msg)
    # client.subscribe("/topic/listen.235", headers={**headers}, callback=on_msg)

    while True:
        print("Sending message")
        await asyncio.sleep(1)
    # client.send("/queue/channel", headers, "Hello World")


def on_msg(msg):
    print("Message received")
    print(msg)


def on_open(ws):
    print("Ok")


def main(args):
    try:
        asyncio.run(hello(uri))
        print("Done")
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(run())
        # loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Process interrupted")
    finally:
        # loop.close()
        logging.info("Successfully shutdown.")


if __name__ == "__main__":
    main(sys.argv)
