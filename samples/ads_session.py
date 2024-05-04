import logging

logging.basicConfig(level=logging.INFO)

import requests
from io import BytesIO

from swibots import (
    BotContext,
    Client,
    CommandEvent,
    CallbackQueryEvent,
    BotCommand,
    InlineMarkup,
    InlineKeyboardButton,
    regexp,
)
from datetime import datetime

BOT_TOKEN = "TOKEN HERE"
AD_TYPE = "VIDEO_1"  # or "VIDEO_2"
AD_ID = "e45206-------8516f557af"
VERIFY_HRS = 12  # verify after 12 hours

app = Client(BOT_TOKEN, is_app=True, home_callback="page")
app.set_bot_commands(
    [
        BotCommand("start", "Starts the bot", True),
        BotCommand("unlock", "Unlock the secret", True),
    ]
)

approvedUsers = {}


@app.on_command("start")
async def onStart(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(
        "Hello, You can unlock the suprise by sending `/unlock` command!"
    )


@app.on_command("unlock")
async def unlockCommand(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    userId = m.user_id
    ttime = approvedUsers.get(userId)
    if ttime and (
        ((datetime.now() - datetime.fromtimestamp(ttime)).total_seconds() / 3600)
        < VERIFY_HRS
    ):
        await m.send("You are already approved!")
        return
    await m.send(
        "Click below button to watch ad and unlock your reward!",
        inline_markup=InlineMarkup(
            [[InlineKeyboardButton("Watch 🎁", callback_data="showAD")]]
        ),
    )


@app.on_callback_query(regexp("showAD"))
async def getRewards(ctx: BotContext[CallbackQueryEvent]):
    """Show ad and unlock rewards"""
    await ctx.event.show_ad(id=AD_ID, ad_type=AD_TYPE, success_callback="watched")


@app.on_callback_query(regexp("watched"))
async def onSuccess(ctx: BotContext[CallbackQueryEvent]):
    """User watched the ad successfully"""
    userId = ctx.event.action_by_id
    approvedUsers[userId] = datetime.now().timestamp()
    m = ctx.event.message
    file = BytesIO(requests.get("https://upload.wikimedia.org/wikipedia/commons/8/8a/1000_USD_note%3B_series_of_1934%3B_obverse.jpg").content)
    file.name = "reward.png"
    await m.send("Thank you for watching the ad!\nHere is your reward!")
    await m.send("", document=file)


app.run()
