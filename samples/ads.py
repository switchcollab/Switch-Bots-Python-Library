import logging
logging.basicConfig(level=logging.INFO)

from swibots import AdButton, AppPage, BotContext, CallbackQueryEvent, Client, Text, CommandEvent, BotCommand

TOKEN = "TOKEN HERE"
VIDEO_1_ID = "AD ID HERE"
VIDEO_2_ID = "AD ID HERE"


client = Client(TOKEN,
             is_app=True,
             home_callback="page")
client.set_bot_commands([
    BotCommand("start", "Get Start messages", True)
])

@client.on_command("start")
async def onStart(ctx: BotContext[CommandEvent]):
    await ctx.event.reply_text("Click below button to open page!",
                               inline_markup=InlineMarkup([[
                                   InlineKeyboardButton("Open Page",
                                                        callback_data="page")
                               ]]))


@client.on_callback_query(regexp("page"))
async def __e(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
            components=[
                Text("Click below button to open ad."),
                AdButton("Watch Ad [1]", callback_data="ad_1"),
                AdButton("Watch Ad [2]", callback_data="ad_2"),
            ]
        )
    await ctx.event.answer(
        callback=page
    )


@client.on_callback_query(regexp("ad_1"))
async def e(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.show_ad(
        ad_type="VIDEO_1",
        id=VIDEO_1_ID,
        success_callback="Success"
        
    )

@client.on_callback_query(regexp("ad_2"))
async def __e(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.show_ad(
        ad_type="VIDEO_2",
        id=VIDEO_2_ID,
        success_callback="Success"
    )

@client.on_callback_query(regexp("Success"))
async def __e(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.answer("Showed", show_alert=True)


client.run()