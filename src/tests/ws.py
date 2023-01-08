import asyncio
import logging
import os
from pathlib import Path
import sys
import time
from switch.utils.stomp import Client
from dotenv import load_dotenv

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

TOKEN = os.getenv('ACCESS_TOKEN') if os.getenv('ACCESS_TOKEN') else ""
uri = "ws://51.158.56.0:8080/comm"
logging.basicConfig(level=logging.DEBUG)

async def run():
    headers = {"Authorization": "Bearer " + TOKEN}

    # websocket.enableTrace(True)
    # ws = websocket.WebSocketApp(uri, header=headers, on_message=on_msg)
    # ws.on_open = on_open
    #ws.run_forever()
    client = Client(uri)

    # connect to the endpoint
    client.connect(headers={**headers})
    client.subscribe("/topic/messages", headers={**headers}, callback=on_msg)
    client.subscribe("/topic/listen.235", headers={**headers}, callback=on_msg)

    #client.send("/queue/channel", headers, "Hello World")

def on_msg(msg):
    print("Message received")
    print(msg)

def on_open(ws):
    print("Ok")

def main(args):
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Process interrupted")                       
    finally:
        loop.close()                                              
        logging.info("Successfully shutdown.") 


if __name__ == '__main__':
    main(sys.argv)
