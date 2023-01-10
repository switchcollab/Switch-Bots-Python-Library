import asyncio
import logging
import os
from dotenv import load_dotenv
env_file = os.path.join(os.path.dirname(__file__), "..","..", ".env")
load_dotenv(env_file)

from switch import config
from switch import SwitchApp
from switch.bots import CommandHandler


TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


async def main():
    app = SwitchApp.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("echo", lambda ctx: print(ctx.request.message.message)))
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())