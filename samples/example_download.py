from swibots import (
    BotApp,
    RegisterCommand,
    BotContext,
    CallbackQueryEvent,
    CommandEvent,
    InlineMarkup,
    InlineKeyboardButton,
    InlineKeyboardColor,
    InlineKeyboardSize,
    regexp,
    CommunityUpdatedEvent,
    MessageEvent,
    Message,
    DownloadProgress,
    MediaUploadRequest,
)
import logging
logging.basicConfig(level=logging.DEBUG)

TOKEN = "YOUR_TOKEN_HERE"

app = BotApp(
    TOKEN,
    "A cool bot with annotations and everything you could possibly want :)"
).register_command([
    RegisterCommand("echo", "Echoes the message", True),
    RegisterCommand("buttons", "Shows buttons", True),
    RegisterCommand("buttonfull", "Shows buttons", True),
    RegisterCommand("back", "Shows buttons", True),
    RegisterCommand("upload", "Reply with media", True),
])


@app.on_command("buttons")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    m.message = f"Please select an option:"

    inline_keyboard = [
        [
            InlineKeyboardButton(text="Option 18", callback_data="option18"),
            InlineKeyboardButton(text="Option 19", callback_data="option19"),
            InlineKeyboardButton(text="Option 20", callback_data="option20"),
        ],
        [
            InlineKeyboardButton(text="Option 33", callback_data="option33"),
            InlineKeyboardButton(text="Option 43", callback_data="option43"),
            InlineKeyboardButton(text="Option 63", callback_data="option63"),
            InlineKeyboardButton(text="Option 73", callback_data="option73"),
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
        inline_keyboard=inline_keyboard,
        color=InlineKeyboardColor.RED,
        size=InlineKeyboardSize.DEFAULT,
    )
    await ctx.bot.send_message(m)


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
        color=InlineKeyboardColor.GREEN,
        size=InlineKeyboardSize.FULL_WIDTH,
    )
    await ctx.bot.send_message(m)


@app.on_command("echo")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    m.message = f"Please select an option:"

    inline_keyboard1 = [
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
        inline_keyboard=inline_keyboard1,
        color=InlineKeyboardColor.RANDOM,
        size=InlineKeyboardSize.DEFAULT,
    )
    await m.reply_text("Please select an option (echo):", InlineMarkup(
        inline_keyboard=inline_keyboard1,
        color=InlineKeyboardColor.RANDOM,
        size=InlineKeyboardSize.DEFAULT,
    ))


@app.on_callback_query()
async def query_callback_handler(ctx: BotContext[CallbackQueryEvent]):
    m = ctx.event.message
    m.message = f"Thank you! I received your callback: {ctx.event.callback_data}"
    m.inline_markup = None
    await ctx.edit_message(m)


@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
    # m = await ctx.prepare_response_message(ctx.event.message)
    # m.message = f"Thank you! I received your message: {ctx.event.message.message}"
    # await ctx.send_message(m)
    print(f"Downloading received message: {ctx.event.message.id}")
    message: Message = ctx.event.message
    if message.media_link is not None:
        print(message.media_link)
        await message.download(in_memory=False, block=False, progress=handle_download_progress)


async def handle_download_progress(progress: DownloadProgress):
    print(f"Downloaded {progress.downloaded} of {progress.total}")


@app.on_community_update()
async def community_update_handler(ctx: BotContext[CommunityUpdatedEvent]):
    print(ctx.event.community_id + " was updated")

# app.run()


@app.on_callback_query()
def show_upload_progress(obj):
    print(f"Uploaded {obj.current} of {obj.readed}")
    if obj == 0:
        return


@app.on_command("upload")
async def upload_handler(ctx: BotContext[CommandEvent]):
    params = ctx.event.params
    media = MediaUploadRequest(
        path=f"downloads/{params}",
        callback=show_upload_progress,
    )

    r = await ctx.event.message.reply_text(f"Here is your file {params}", media=media)
    print(r)

app.run()
