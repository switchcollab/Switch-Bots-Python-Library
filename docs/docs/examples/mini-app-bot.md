# Mini App Bot Example

This example demonstrates how to create a bot that launches a mini app using SwiBots. The mini app showcases various UI components and interactions.

## Prerequisites

Before you begin, make sure you have:

1. Installed SwiBots (`pip install swibots`)
2. Obtained a bot token from the Switch platform

## Step-by-Step Tutorial

### Step 1: Set up the bot

First, let's import the necessary modules and set up the basic structure of our bot:

```python
import logging
from swibots import (
    Client, BotContext, CommandEvent, CallbackQueryEvent, BotCommand,
    AppPage, Text, Button, ButtonGroup, Image, VideoPlayer, Grid, GridItem,
    SearchBar, Dropdown, ListItem, ScreenType, TextSize,
    InlineKeyboardButton, InlineMarkup
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_BOT_TOKEN_HERE"

app = Client(TOKEN, is_app=True, home_callback="open_app")
app.set_bot_commands([BotCommand("start", "Open the mini app", True)])
```

### Step 2: Create the start command

Now, let's create a handler for the `/start` command:

```python
@app.on_command("start")
async def start_command(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(
        "Welcome to the Mini App Example! Click the button below to open the app.",
        inline_markup=InlineMarkup([[
            InlineKeyboardButton("Open Mini App", callback_data="open_app", app=True)
        ]])
    )
```

### Step 3: Design the main app page

Create a function to handle the main app page:

```python
@app.on_callback_query(regexp("open_app"))
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
```

### Step 4: Add a video player page

Create a function to display a video player:

```python
@app.on_callback_query(regexp("show_video"))
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
```

### Step 5: Add a grid view page

Create a function to display a grid of items:

```python
@app.on_callback_query(regexp("show_grid"))
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
```

### Step 6: Handle user interactions

Add functions to handle various user interactions:

```python
@app.on_callback_query(regexp("search"))
async def handle_search(ctx: BotContext[CallbackQueryEvent]):
    query = ctx.event.details.get("searchQuery")
    if query:
        await ctx.event.answer(f"You searched for: {query}", show_alert=True)
    else:
        await ctx.event.answer("Please enter a search query", show_alert=True)

@app.on_callback_query(regexp("option_"))
async def handle_dropdown(ctx: BotContext[CallbackQueryEvent]):
    option = ctx.event.callback_data.split("_")[1]
    await ctx.event.answer(f"You selected Option {option}", show_alert=True)

@app.on_callback_query(regexp("grid_item_"))
async def handle_grid_item(ctx: BotContext[CallbackQueryEvent]):
    item = ctx.event.callback_data.split("_")[-1]
    await ctx.event.answer(f"You clicked Grid Item {item}", show_alert=True)

@app.on_callback_query(regexp("image_clicked"))
async def handle_image_click(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.answer("You clicked the image!", show_alert=True)
```

### Step 7: Run the bot

Finally, add the code to run the bot:

```python
if __name__ == "__main__":
    app.run()
```

## Running the Bot

To run the bot, save the complete code in a file (e.g., `mini_app_bot.py`) and execute it:

```bash
python mini_app_bot.py
```

## Using the Bot

1. Start a conversation with your bot and send the `/start` command.
2. Click the "Open Mini App" button to launch the mini app.
3. Interact with various components in the mini app:
   - Click on the image to trigger an alert.
   - Use the "Show Video" and "Show Grid" buttons to navigate to different screens.
   - Try the search bar by entering a query.
   - Select an option from the dropdown menu.
   - Click on grid items in the grid view.

## Features Demonstrated

This example showcases the following SwiBots features:

1. Creating a mini app with various UI components:
   - Text
   - Image
   - Buttons and ButtonGroups
   - Video Player
   - Grid and GridItems
   - Search Bar
   - Dropdown menu
2. Handling user interactions with different components.
3. Navigating between different screens within the mini app.
4. Using callbacks to update the app's content dynamically.

## Note

This is a basic implementation to demonstrate the capabilities of SwiBots mini apps. For a production-ready bot, consider adding error handling, input validation, and more advanced features tailored to your specific use case.

<details>
<summary>Complete Code</summary>

```python
import logging
from swibots import (
    Client, BotContext, CommandEvent, CallbackQueryEvent, BotCommand,
    AppPage, Text, Button, ButtonGroup, Image, VideoPlayer, Grid, GridItem,
    SearchBar, Dropdown, ListItem, ScreenType, TextSize,
    InlineKeyboardButton, InlineMarkup, regexp
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

@app.on_callback_query(regexp("open_app"))
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

@app.on_callback_query(regexp("show_video"))
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

@app.on_callback_query(regexp("show_grid"))
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

@app.on_callback_query(regexp("search"))
async def handle_search(ctx: BotContext[CallbackQueryEvent]):
    query = ctx.event.details.get("searchQuery")
    if query:
        await ctx.event.answer(f"You searched for: {query}", show_alert=True)
    else:
        await ctx.event.answer("Please enter a search query", show_alert=True)

@app.on_callback_query(regexp("option_"))
async def handle_dropdown(ctx: BotContext[CallbackQueryEvent]):
    option = ctx.event.callback_data.split("_")[1]
    await ctx.event.answer(f"You selected Option {option}", show_alert=True)

@app.on_callback_query(regexp("grid_item_"))
async def handle_grid_item(ctx: BotContext[CallbackQueryEvent]):
    item = ctx.event.callback_data.split("_")[-1]
    await ctx.event.answer(f"You clicked Grid Item {item}", show_alert=True)

@app.on_callback_query(regexp("image_clicked"))
async def handle_image_click(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.answer("You clicked the image!", show_alert=True)

if __name__ == "__main__":
    app.run()
```

</details>