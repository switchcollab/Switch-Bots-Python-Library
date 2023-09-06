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

from swibots import (
    BotApp,
    BotContext,
    CommandEvent,
    MessageEvent,
    CallbackQueryEvent,
    filters,
    InlineKeyboardButton,
    InlineMarkup,
    BotCommand,
)

from swibots.bots.handlers import (
    MessageHandler,
    UnknownCommandHandler,
    CallbackQueryHandler,
    CommandHandler,
)
import logging

env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_file)


TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


async def echo_handler(ctx: BotContext[CommandEvent]):
    text = ctx.event.params or "No args"
    message = f"Your message: {text}"
    await ctx.event.message.reply_text(message)


async def buttons_handler(ctx: BotContext[CommandEvent]):
    message = f"Please select an option:"

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

    inline_markup = InlineMarkup(inline_keyboard=inline_keyboard)
    await ctx.event.message.reply_text(message, inline_markup=inline_markup)


async def message_handler(ctx: BotContext[MessageEvent]):
    message = f"Thank you! I received your message: {ctx.event.message.message}"
    await ctx.event.message.reply_text(message)


async def unkown_command_handler(ctx: BotContext[CommandEvent]):
    message = f"Unknown command: {ctx.event.command}"
    await ctx.event.message.reply_text(message)


async def query_callback_handler(ctx: BotContext[CallbackQueryEvent]):
    message = f"Thank you! I received your callback: {ctx.event.callback_query.data}"
    await ctx.event.message.edit_text(message)


app = BotApp(token=TOKEN).set_bot_commands(
    [
        BotCommand("echo", "Echoes back the message", True),
        BotCommand("buttons", "Shows buttons", True),
        BotCommand("help", "Shows help", True),
    ]
)


app.add_handler(
    CommandHandler(
        command="echo",
        callback=echo_handler,
    )
)
app.add_handler(CommandHandler(command="buttons", callback=buttons_handler))
app.add_handler(CallbackQueryHandler(callback=query_callback_handler))
app.add_handler(
    MessageHandler(
        callback=message_handler, filter=filters.text("hello") | filters.text("hi")
    )
)
app.add_handler(UnknownCommandHandler(callback=unkown_command_handler))


app.run()
