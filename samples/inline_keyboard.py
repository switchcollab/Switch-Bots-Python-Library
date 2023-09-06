import logging
import os
from dotenv import load_dotenv

from swibots import (
    BotApp,
    BotContext,
    CallbackQueryEvent,
    CommandEvent,
    BotCommand,
    InlineMarkup,
    InlineKeyboardButton,
    regexp,
)


env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_file)


TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


# initialize the app and register commands
app = BotApp(
    TOKEN,
).set_bot_commands([BotCommand("buttons", "Get Buttons")])


# register buttons command
@app.on_command("buttons")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    try:
        m = ctx.event.message
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
        await ctx.event.reply_text(message, inline_markup=inline_markup)
    except Exception as e:
        logger.exception(f"Error while processing event: {e}")
        raise e


# handle callback query
@app.on_callback_query(regexp(r"option\d"))
async def callback_query_handler(ctx: BotContext[CallbackQueryEvent]):
    try:
        message = ctx.event.message
        await message.edit_text(
            f"Option with data: {ctx.event.callback_data} selected!"
        )
    except Exception as e:
        logger.exception(f"Error while processing event: {e}")
        raise e


app.run()
