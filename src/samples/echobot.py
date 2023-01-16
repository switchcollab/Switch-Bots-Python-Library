import asyncio
import logging
import os
from dotenv import load_dotenv

from switch import SwitchApp
from switch.api.bot.models.bot_command_info import BotCommandInfo
from switch.api.chat.events import CallbackQueryEvent, CommandEvent, MessageEvent
from switch.api.chat.models import InlineKeyboardButton, InlineMarkup
from switch.bots import BotContext
from switch.bots import filters, Decorators

from switch.bots.handlers import (
    MessageHandler,
    UnknownCommandHandler,
    CallbackQueryHandler,
    CommandHandler,
)

env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_file)


TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


async def echo_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    text = ctx.event.params or "No args"
    m.message = f"Your message: {text}"
    await ctx.bot.send_message(m)


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

    m.inline_markup = InlineMarkup(inline_keyboard=inline_keyboard)
    await ctx.bot.send_message(m)


async def message_handler(ctx: BotContext[MessageEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    m.message = f"Thank you! I received your message: {ctx.event.message.message}"
    await ctx.bot.send_message(m)


async def unkown_command_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    m.message = f"Unknown command: {ctx.event.command}"
    await ctx.bot.send_message(m)


async def query_callback_handler(ctx: BotContext[CallbackQueryEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.callback_query.message)
    m.message = f"Thank you! I received your callback: {ctx.event.callback_query.data}"
    m.inline_markup = None
    await ctx.bot.edit_message(m)


async def main():
    app = (
        SwitchApp.builder()
        .token(TOKEN)
        .commands(
            [
                BotCommandInfo("echo", "Echoes back the message", True),
                BotCommandInfo("buttons", "Shows buttons", True),
                BotCommandInfo("help", "Shows help", True),
            ]
        )
        .description("Super cool!")
        .build()
    )

    try:
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

        await app.start()
    finally:
        await app.__aexit__()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
