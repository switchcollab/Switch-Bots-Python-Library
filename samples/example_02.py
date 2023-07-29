import os
from swibots import (
    BotApp,
    RegisterCommand,
    BotContext,
    CallbackQueryEvent,
    CommandEvent,
    InlineMarkup,
    InlineKeyboardButton,
    regexp,
    CommunityUpdatedEvent,
    MessageEvent,
    Message,
)
import logging
from dotenv import load_dotenv


env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_file)


TOKEN = os.getenv("TOKEN")


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = BotApp(
    TOKEN,
    "A cool bot with annotations and everything you could possibly want :)"
).register_command([
    RegisterCommand("echo", "Echoes the message", True),
    RegisterCommand("buttons", "Shows buttons", True),
    RegisterCommand("buttonfull", "Shows buttons", True),
    RegisterCommand("Back", "Shows buttons", True),
])

app = BotApp(
    TOKEN,
    "A cool bot with annotations and everything you could possibly want :)"
).register_command([
    RegisterCommand("echo", "Echoes the message", True),
    RegisterCommand("buttons", "Shows buttons", True),
    RegisterCommand("buttonfull", "Shows buttons", True),
    RegisterCommand("Back", "Shows buttons", True),
])


@app.on_command("buttons")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    # m = await ctx.bot.prepare_response_message(ctx.event.message)
    # m.message = f"Please select an option:"

    inline_keyboard = [
        [
            InlineKeyboardButton(text="Optioniablek",
                                 callback_data="option53"),
            InlineKeyboardButton(text="Unitedstates",
                                 callback_data="option03"),
        ],
        [
            InlineKeyboardButton(text="Go Back on Press",
                                 callback_data="option543"),
        ],
        [
            InlineKeyboardButton(text="Go Back on Press for more Movies haha",
                                 callback_data="option543"),
        ],
    ]

    inline_markup = InlineMarkup(
        inline_keyboard=inline_keyboard,
    )
    await ctx.event.message.reply_text(f"Please select an option:",
                                       inline_markup)


@app.on_command("test")
async def test_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.prepare_response_message(ctx.event.message)
    m.message = "Test command received"
    await ctx.send_message(m)


@app.on_command("buttonfull")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    m.message = f"Please select an option:"

    inline_keyboard1 = [
        [
            InlineKeyboardButton(text="Option 1111", callback_data="option1"),
            InlineKeyboardButton(text="Option 1112", callback_data="option2"),
            InlineKeyboardButton(text="Option 1115", callback_data="option5"),
        ],
        [
            InlineKeyboardButton(text="Option 18", callback_data="option18"),
            InlineKeyboardButton(text="Option 19", callback_data="option19"),
            InlineKeyboardButton(text="Option 20", callback_data="option20"),
        ],
        [
            InlineKeyboardButton(text="Optioniablek",
                                 callback_data="option53"),
            InlineKeyboardButton(text="Unitedstates",
                                 callback_data="option03"),
        ],
        [
            InlineKeyboardButton(text="Go Back on Press",
                                 callback_data="option543"),
        ],
        [
            InlineKeyboardButton(text="Go Back on Press for more Movies haha",
                                 callback_data="option543"),
        ],
    ]

    m.inline_markup = InlineMarkup(
        inline_keyboard=inline_keyboard1,
    )
    await ctx.bot.send_message(m)


@app.on_command("echo")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    m.message = f"Please select an option:"

    inline_keyboard2 = [
        [
            InlineKeyboardButton(text="Option 1", callback_data="option1"),
            InlineKeyboardButton(text="Option 2", callback_data="option2"),
        ],
        [
            InlineKeyboardButton(text="Option 3", callback_data="option3"),
            InlineKeyboardButton(text="Option 4", callback_data="option4"),
            InlineKeyboardButton(text="Option 5", callback_data="option5"),
            InlineKeyboardButton(text="Option 6", callback_data="option6"),
        ],
    ]

    m.inline_markup = InlineMarkup(
        inline_keyboard=inline_keyboard2,
    )
    await ctx.bot.send_message(m)


@app.on_callback_query()
async def query_callback_handler(ctx: BotContext[CallbackQueryEvent]):
    m = ctx.event.message
    m.message = f"Thank you! I received your callback: {ctx.event.callback_data}"
    inline_keyboard3 = [[
        InlineKeyboardButton(text="Option 1", callback_data="option1"),
        InlineKeyboardButton(text="Option 2", callback_data="option2"),
    ], [
        InlineKeyboardButton(text="Back to Home", callback_data="back"),
    ]]
    m.inline_markup = InlineMarkup(
        inline_keyboard=inline_keyboard3,
    )
    await ctx.bot.edit_message(m)


@app.on_callback_query(regexp(r"back"))
async def callback_query_handler(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.message.edit_text(f"thanks selected!")


@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
    await ctx.event.message.reply_text(
        f"Thank you! I received your message: {ctx.event.message.message}")


@app.on_community_update()
async def community_update_handler(ctx: BotContext[CommunityUpdatedEvent]):
    print(ctx.event.community_id + " was updated")


app.run()
