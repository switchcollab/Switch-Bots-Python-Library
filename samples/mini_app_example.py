import logging
import re
from swibots import (
    Client,
    BotContext,
    CommandEvent,
    CallbackQueryEvent,
    BotCommand,
    AppPage,
    Text,
    Button,
    ButtonGroup,
    Image,
    VideoPlayer,
    Carousel,
    Grid,
    GridItem,
    SearchBar,
    Dropdown,
    ListItem,
    ScreenType,
    TextSize,
    InlineKeyboardButton,
    InlineMarkup,
    regexp
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_BOT_TOKEN_HERE"

app = Client(TOKEN, is_app=True, home_callback="open_app")
app.set_bot_commands([BotCommand("start", "Open the mini app", True)])

@app.on_command("start")
async def start_command(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(
        "Welcome to the Mini App Example! Click the button below to open the app.",
        inline_markup=InlineMarkup([[
            InlineKeyboardButton("Open Mini App", callback_data="open_app", app=True)
        ]])
    )

@app.on_callback_query(regexp('open_app'))
async def open_app(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Welcome to the Mini App Example!", size=TextSize.LARGE),
            Image("https://example.com/sample-image.jpg", callback_data="image_clicked"),
            ButtonGroup([
                Button("Show Video", callback_data="show_video"),
                Button("Show Grid", callback_data="show_grid"),
            ]),
            SearchBar(callback_data="search"),
            Dropdown(
                "Select an option",
                options=[
                    ListItem("Option 1", callback_data="option_1"),
                    ListItem("Option 2", callback_data="option_2"),
                    ListItem("Option 3", callback_data="option_3"),
                ]
            ),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp('show_video'))
async def show_video(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Video Player Example", size=TextSize.MEDIUM),
            VideoPlayer("https://example.com/sample-video.mp4", title="Sample Video"),
            Button("Back to Home", callback_data="open_app"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp('show_grid'))
async def show_grid(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Grid Example", size=TextSize.MEDIUM),
            Grid(
                title="Sample Grid",
                options=[
                    GridItem("Item 1", "https://example.com/icon1.png", callback_data="grid_item_1"),
                    GridItem("Item 2", "https://example.com/icon2.png", callback_data="grid_item_2"),
                    GridItem("Item 3", "https://example.com/icon3.png", callback_data="grid_item_3"),
                    GridItem("Item 4", "https://example.com/icon4.png", callback_data="grid_item_4"),
                ]
            ),
            Button("Back to Home", callback_data="open_app"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp('search'))
async def handle_search(ctx: BotContext[CallbackQueryEvent]):
    query = ctx.event.details.get("searchQuery")
    if query:
        await ctx.event.answer(f"You searched for: {query}", show_alert=True)
    else:
        await ctx.event.answer("Please enter a search query", show_alert=True)

@app.on_callback_query(regexp('option_.*'))
async def handle_dropdown(ctx: BotContext[CallbackQueryEvent]):
    option = ctx.event.callback_data.split("_")[1]
    await ctx.event.answer(f"You selected Option {option}", show_alert=True)

@app.on_callback_query(regexp('grid_item_.*'))
async def handle_grid_item(ctx: BotContext[CallbackQueryEvent]):
    item = ctx.event.callback_data.split("_")[-1]
    await ctx.event.answer(f"You clicked Grid Item {item}", show_alert=True)

@app.on_callback_query(regexp('image_clicked'))
async def handle_image_click(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.answer("You clicked the image!", show_alert=True)

if __name__ == "__main__":
    app.run()