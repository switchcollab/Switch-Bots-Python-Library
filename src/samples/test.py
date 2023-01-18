import logging
import os
from dotenv import load_dotenv

from switch import (
    BotApp,
    RegisterCommand,
    BotContext,
    MessageEvent,
    CallbackQueryEvent,
    CommandEvent,
    InlineMarkup,
    InlineKeyboardButton,
    CommunityUpdatedEvent,
    InlineKeyboardColor,
    InlineKeyboardSize,
)


env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_file)


TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.DEBUG)

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


@app.on_command("buttons")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    m.message = f"Please select an option:"

    inline_keyboard = [
        [
            InlineKeyboardButton(text="Option 1", callback_data="option1"),
            InlineKeyboardButton(text="Option 2", callback_data="option2"),
        ],
        [
            InlineKeyboardButton(text="Option 3", callback_data="option3"),
            InlineKeyboardButton(text="Option 4", callback_data="option4"),
        ],
    ]

    m.inline_markup = InlineMarkup(
        inline_keyboard=inline_keyboard,
        color=InlineKeyboardColor.RANDOM,
        size=InlineKeyboardSize.DEFAULT,
    )
    await ctx.bot.send_message(m)


@app.on_command("test")
async def test_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.prepare_response_message(ctx.event.message)
    m.message = "Test command received"
    await ctx.send_message(m)


@app.on_command("echo")
async def echo_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.prepare_response_message(ctx.event.message)
    text = ctx.event.params or "Nothing to echo"
    m.message = f"Your message: {text}"
    await ctx.send_message(m)


@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
    m = await ctx.prepare_response_message(ctx.event.message)
    m.message = f"Thank you! I received your message: {ctx.event.message.message}"
    await ctx.send_message(m)


@app.on_callback_query()
async def query_callback_handler(ctx: BotContext[CallbackQueryEvent]):
    m = ctx.event.message
    m.message = f"Thank you! I received your callback: {ctx.event.callback_data}"
    m.inline_markup = None
    await ctx.edit_message(m)


@app.on_community_update()
async def community_update_handler(ctx: BotContext[CommunityUpdatedEvent]):
    print(ctx.event.community_id + " was updated")


app.run()
