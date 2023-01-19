import logging
import os
from dotenv import load_dotenv

from pyswitch import BotApp, RegisterCommand, BotContext, MessageEvent, CallbackQueryEvent


env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_file)


TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


# initialize the app and register commands
app = BotApp(
    TOKEN, "A cool bot with annotations and everything you could possibly want :)"
).register_command(
    [
        RegisterCommand("test", "Test command", True),
        RegisterCommand("echo", "Echoes the message", True),
        RegisterCommand("buttons", "Shows buttons", True),
    ]
)


@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
    m = await ctx.prepare_response_message(ctx.event.message)
    m.message = f"Thank you! I received your message: {ctx.event.message.message}"
    await ctx.send_message(m)


@app.on_callback_query()
async def query_callback_handler(ctx: BotContext[CallbackQueryEvent]):
    m = await ctx.prepare_response_message(ctx.event.message)
    m.message = f"Thank you! I received your callback: {ctx.event.callback_data}"
    m.inline_markup = None
    await ctx.edit_message(m)


app.run()
