import logging, sys

logging.basicConfig(level=logging.INFO)
from asyncio import create_subprocess_shell, subprocess, create_subprocess_exec
from swibots import (
    BotApp,
    Dropdown,
    Icon,
    CommandEvent,
    Embed,
    CallbackQueryEvent,
    BotCommand,
    VideoPlayer,
    Client,
    Carousel,
    InlineKeyboardButton,
    InlineMarkup,
    Image,
    Grid,
    GridItem,
    ListItem,
    BotContext,
    regexp,
    AppPage,
    ButtonGroup,
    AppBar,
    TextSize,
    Text,
    ScreenType,
    Button,
    SearchBar,
    SearchHolder,
)

BOT_TOKEN = "Token here"

app = Client(
    BOT_TOKEN,
    app_bar=AppBar(),
)

app.set_bot_commands([BotCommand("start", "Get start message", True)])


@app.on_callback_query()
async def onCallback(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.message.send(ctx.event.callback_data)


@app.on_command("start")
async def getStart(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    await m.reply_text(
        "Click below button to open app..",
        inline_markup=InlineMarkup(
            [[InlineKeyboardButton("Open APP", callback_data="open", app=True)]]
        ),
    )


@app.on_callback_query(regexp("open$"))
async def openAPP(ctx: BotContext[CallbackQueryEvent]):
    callback = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text(f"Hi {ctx.event.action_by.name}"),
            SearchHolder(callback_data="showsearch"),
            Image(
                "https://images.unsplash.com/photo-1704531815335-dab68018e8a9",
                callback_data="image",
            ),
            ButtonGroup(
                [
                    Button("Embed", callback_data="embed"),
                    Button("Video Player", callback_data="video"),
                    Button("Carousel", callback_data="carousel"),
                ]
            ),
            ButtonGroup(
                buttons=[
                    Button("Grid View", callback_data="grid"),
                    Button("Horizontal", callback_data="grid1"),
                ]
            ),
            Button("Bottom Sheet", callback_data="bottom"),
        ],
    )
    await ctx.event.answer(callback=callback)
    print(callback.to_json())


@app.on_callback_query(regexp("showsearch$"))
async def openAPP(ctx: BotContext[CallbackQueryEvent]):
    callback = AppPage(
        screen=ScreenType.SCREEN, components=[SearchBar(callback_data="search")]
    )
    await ctx.event.answer(callback=callback)
    print(callback.to_json())


@app.on_callback_query(regexp("search$"))
async def openAPP(ctx: BotContext[CallbackQueryEvent]):
    query = ctx.event.details.get("searchQuery")
    if not query:
        return await ctx.event.answer("Provide search query", show_alert=True)
    await ctx.event.answer(f"You Searched for {query}", show_alert=True)


@app.on_callback_query(regexp("bottom$"))
async def openAPP(ctx: BotContext[CallbackQueryEvent]):
    callback = AppPage(
        screen=ScreenType.BOTTOM,
        components=[
            Text("Choose your favorite fruit..", size=TextSize.SMALL),
            Dropdown(
                "Search Entries",
                options=[
                    ListItem(item, callback_data=f"click|{item}")
                    for item in ["Apple", "Mango", "Orange", "Grapes", "Papaya"]
                ],
            ),
        ],
    )
    await ctx.event.answer(callback=callback)
    print(callback.to_json())


@app.on_callback_query(regexp("grid(.*)"))
async def openAPP(ctx: BotContext[CallbackQueryEvent]):
    horizontal = bool(ctx.event.callback_data[4:])
    callback = AppPage(
        screen=ScreenType.SCREEN,
        layouts=[
            Grid(
                title="Grid Title",
                horizontal=horizontal,
                options=[
                    GridItem(
                        "title",
                        "https://img.icons8.com/?size=256&id=DAKNDASC9B0G&format=png",
                        callback_data="new",
                    )
                    for _ in range(10 if horizontal else 30)
                ],
            )
            for _ in range(3 if horizontal else 1)
        ],
    )
    await ctx.event.answer(callback=callback)
    print(callback.to_json())


@app.on_callback_query(regexp("carousel$"))
async def openAPP(ctx: BotContext[CallbackQueryEvent]):
    callback = AppPage(
        screen=ScreenType.SCREEN,
        layouts=[
            Carousel(
                [
                    Image(
                        "https://images.unsplash.com/photo-1704531815335-dab68018e8a9",
                        callback_data="image1",
                    ),
                    Image(
                        "https://images.unsplash.com/photo-1704531815335-dab68018e8a9",
                        callback_data="image2",
                    ),
                    Image(
                        "https://images.unsplash.com/photo-1704531815335-dab68018e8a9",
                        callback_data="image3",
                    ),
                ]
            )
            for _ in range(3)
        ],
    )
    await ctx.event.answer(callback=callback)
    print(callback.to_json())


@app.on_callback_query(regexp("video$"))
async def openAPP(ctx: BotContext[CallbackQueryEvent]):
    proc = await create_subprocess_exec(
        sys.executable,
        *[
            "-m",
            "yt_dlp",
            "-f",
            "bestaudio+bestvideo",
            "-g",
            "https://youtu.be/-Jros0sg3CM",
        ],
        stdout=subprocess.PIPE,
    )
    await proc.wait()
    out = (await proc.stdout.read()).decode().strip()
    print(out)
    url = out.split("\n")[-1]
    print(url)
    callback = AppPage(
        screen=ScreenType.SCREEN,
        components=[VideoPlayer(url, title="Trending of 2023")],
    )
    await ctx.event.answer(callback=callback)
    print(callback.to_json())


@app.on_callback_query(regexp("embed$"))
async def openAPP(ctx: BotContext[CallbackQueryEvent]):
    callback = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Embed(
                "https://switchcollab.github.io/Switch-Bots-Python-Library/",
                full_screen=True,
            )
        ],
    )
    await ctx.event.answer(callback=callback)
    print(callback.to_json())


app.run()
