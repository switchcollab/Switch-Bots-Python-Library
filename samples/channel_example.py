import os  # noqa
import sys  # noqa
import inspect  # noqa

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe()))
)  # noqa
parentdir = os.path.dirname(currentdir)  # noqa
sys.path.insert(0, parentdir)  # noqa
from dotenv import load_dotenv

env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")  # noqa
load_dotenv(env_file)  # noqa

from swibots import BotApp, BotContext, ChannelCreatedEvent, Message
from swibots.bots.filters import channel
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_file)


TOKEN = os.getenv("TOKEN")


app = BotApp(TOKEN, "your bot description")


@app.on_channel_created(channel("d71e33f9-8e12-491f-b041-d02ea6ec6520"))
async def channel_created_handler(ctx: BotContext[ChannelCreatedEvent]):
    new_channel_name = ctx.event.channel.name
    new_channel_id = ctx.event.channel.id
    m = Message()
    m.message = f"Channel {new_channel_name} created with id {new_channel_id}"
    m.community_id = ctx.event.community.id
    m.channel_id = "d71e33f9-8e12-491f-b041-d02ea6ec6520"
    await ctx.send_message(message=m)


app.run()
