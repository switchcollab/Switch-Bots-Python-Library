# Restaurant Menu and Order Bot Example

This example demonstrates a real-world use case of a mini app using SwiBots. The bot creates a restaurant menu app where users can browse menu items, add them to a cart, and place an order.

## Prerequisites

Before you begin, make sure you have:

1. Installed SwiBots (`pip install swibots`)
2. Obtained a bot token from the Switch platform

## The Code

Here's the complete code for our restaurant menu bot:

```python
import logging
from swibots import (
    Client, BotContext, CommandEvent, CallbackQueryEvent, BotCommand,
    AppPage, Text, Button, ButtonGroup, Image, Grid, GridItem,
    ScreenType, TextSize, InlineKeyboardButton, InlineMarkup, regexp
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_BOT_TOKEN_HERE"

app = Client(TOKEN, is_app=True, home_callback="show_menu")
app.set_bot_commands([BotCommand("start", "Open the restaurant menu", True)])

# Simulated menu data
menu = {
    "appetizers": [
        {"id": "app1", "name": "Bruschetta", "price": 7.99, "image": "https://example.com/bruschetta.jpg"},
        {"id": "app2", "name": "Mozzarella Sticks", "price": 6.99, "image": "https://example.com/mozzarella.jpg"},
    ],
    "main_courses": [
        {"id": "main1", "name": "Spaghetti Carbonara", "price": 14.99, "image": "https://example.com/carbonara.jpg"},
        {"id": "main2", "name": "Grilled Salmon", "price": 18.99, "image": "https://example.com/salmon.jpg"},
    ],
    "desserts": [
        {"id": "des1", "name": "Tiramisu", "price": 6.99, "image": "https://example.com/tiramisu.jpg"},
        {"id": "des2", "name": "Cheesecake", "price": 5.99, "image": "https://example.com/cheesecake.jpg"},
    ]
}

# User cart
user_carts = {}

@app.on_command("start")
async def start_command(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(
        "Welcome to our restaurant! Click the button below to see our menu.",
        inline_markup=InlineMarkup([[
            InlineKeyboardButton("View Menu", callback_data="show_menu", app=True)
        ]])
    )

@app.on_callback_query(regexp("show_menu"))
async def show_menu(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Our Menu", size=TextSize.LARGE),
            ButtonGroup([
                Button("Appetizers", callback_data="menu_appetizers"),
                Button("Main Courses", callback_data="menu_main_courses"),
                Button("Desserts", callback_data="menu_desserts"),
            ]),
            Button("View Cart", callback_data="view_cart"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("menu_"))
async def show_category(ctx: BotContext[CallbackQueryEvent]):
    category = ctx.event.callback_data.split("_")[1]
    items = menu[category]
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text(f"{category.capitalize()}", size=TextSize.LARGE),
            Grid(
                title="Menu Items",
                options=[
                    GridItem(
                        f"{item['name']}\n${item['price']:.2f}",
                        item['image'],
                        callback_data=f"add_to_cart_{item['id']}"
                    ) for item in items
                ]
            ),
            Button("Back to Menu", callback_data="show_menu"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("add_to_cart_"))
async def add_to_cart(ctx: BotContext[CallbackQueryEvent]):
    item_id = ctx.event.callback_data.split("_")[-1]
    user_id = ctx.event.action_by_id
    
    if user_id not in user_carts:
        user_carts[user_id] = {}
    
    if item_id in user_carts[user_id]:
        user_carts[user_id][item_id] += 1
    else:
        user_carts[user_id][item_id] = 1
    
    await ctx.event.answer("Item added to cart!", show_alert=True)

@app.on_callback_query(regexp("view_cart"))
async def view_cart(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    cart = user_carts.get(user_id, {})
    
    if not cart:
        await ctx.event.answer("Your cart is empty!", show_alert=True)
        return
    
    total = 0
    cart_items = []
    for item_id, quantity in cart.items():
        item = next(item for category in menu.values() for item in category if item['id'] == item_id)
        subtotal = item['price'] * quantity
        total += subtotal
        cart_items.append(f"{item['name']} x{quantity}: ${subtotal:.2f}")
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Your Cart", size=TextSize.LARGE),
            Text("\n".join(cart_items), size=TextSize.MEDIUM),
            Text(f"Total: ${total:.2f}", size=TextSize.LARGE),
            ButtonGroup([
                Button("Place Order", callback_data="place_order"),
                Button("Back to Menu", callback_data="show_menu"),
            ]),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("place_order"))
async def place_order(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    if user_id in user_carts:
        del user_carts[user_id]
        await ctx.event.answer("Your order has been placed! Thank you for your purchase.", show_alert=True)
    else:
        await ctx.event.answer("Your cart is empty!", show_alert=True)

if __name__ == "__main__":
    app.run()
```

## Features Demonstrated

This example showcases the following SwiBots features:

1. Creating a mini app with a practical, real-world use case
2. Using various UI components:
   - Text
   - Buttons and ButtonGroups
   - Grid and GridItems
3. Implementing navigation between different screens
4. Maintaining user state (shopping cart) across interactions
5. Handling user actions like adding items to cart and placing orders

## How It Works

1. The bot starts with a welcome message and a button to view the menu.
2. The main menu screen shows categories (Appetizers, Main Courses, Desserts) and a "View Cart" button.
3. Each category screen displays menu items in a grid, allowing users to add items to their cart.
4. The cart screen shows the selected items, quantities, and total price, with options to place the order or return to the menu.
5. When an order is placed, the cart is cleared, and a confirmation message is shown.

This example demonstrates how to create a more complex, interactive mini app that could be used by real businesses to showcase their products and handle customer orders.

## Running the Bot

To run the bot, save the complete code in a file (e.g., `restaurant_menu_bot.py`) and execute it:

```bash
python restaurant_menu_bot.py
```

## Note

This is a simplified implementation for demonstration purposes. In a production environment, you would need to add error handling, integrate with a real database for menu items and orders, implement user authentication, and add more features like order tracking and payment processing.