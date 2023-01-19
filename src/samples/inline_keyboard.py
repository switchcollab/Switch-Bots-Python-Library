import logging
import os
from dotenv import load_dotenv

from pyswitch import (
    BotApp,
    BotContext,
    CallbackQueryEvent,
    CommandEvent,
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
    auto_update_bot=False,  # disable auto update bot info
)


# register buttons command
@app.on_command("buttons")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    try:
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

        m.inline_markup = InlineMarkup(inline_keyboard=inline_keyboard)
        await ctx.bot.send_message(m)
    except Exception as e:
        logger.exception(f"Error while processing event: {e}")
        raise e


# handle callback query
@app.on_callback_query(regexp(r"option\d"))
async def callback_query_handler(ctx: BotContext[CallbackQueryEvent]):
    try:
        message = ctx.event.message
        message.message = f"Option with data: {ctx.event.callback_data} selected!"
        await ctx.bot.edit_message(message)
    except Exception as e:
        logger.exception(f"Error while processing event: {e}")
        raise e


app.run()
