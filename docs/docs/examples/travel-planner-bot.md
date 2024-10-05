# Travel Planner Bot Example

This example demonstrates a comprehensive real-world use case of a mini app using SwiBots. The bot creates a travel planning application where users can explore destinations, check weather forecasts, convert currencies, and manage their travel itineraries.

## Prerequisites

Before you begin, make sure you have:

1. Installed SwiBots (`pip install swibots`)
2. Obtained a bot token from the Switch platform
3. Signed up for free API keys from OpenWeatherMap and ExchangeRate-API (for demonstration purposes)

## The Code

Here's the complete code for our travel planner bot:

```python
import logging
import aiohttp
from datetime import datetime, timedelta
from swibots import (
    Client, BotContext, CommandEvent, CallbackQueryEvent, BotCommand,
    AppPage, Text, Button, ButtonGroup, Image, Grid, GridItem,
    ScreenType, TextSize, InlineKeyboardButton, InlineMarkup,
    Carousel, VideoPlayer, SearchBar, Dropdown, ListItem, EmbeddedMedia
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_BOT_TOKEN_HERE"
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
EXCHANGE_API_KEY = "YOUR_EXCHANGERATE_API_KEY"

app = Client(TOKEN, is_app=True, home_callback="main_menu")
app.set_bot_commands([BotCommand("start", "Open the travel planner", True)])

# Simulated destination data
destinations = {
    "paris": {
        "name": "Paris",
        "country": "France",
        "description": "The City of Light",
        "image": "https://example.com/paris.jpg",
        "video": "https://example.com/paris_promo.mp4"
    },
    "tokyo": {
        "name": "Tokyo",
        "country": "Japan",
        "description": "A blend of the ultramodern and the traditional",
        "image": "https://example.com/tokyo.jpg",
        "video": "https://example.com/tokyo_promo.mp4"
    },
    "new_york": {
        "name": "New York City",
        "country": "USA",
        "description": "The Big Apple",
        "image": "https://example.com/nyc.jpg",
        "video": "https://example.com/nyc_promo.mp4"
    }
}

# User itineraries
user_itineraries = {}

@app.on_command("start")
async def start_command(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(
        "Welcome to the Travel Planner! Let's start planning your next adventure.",
        inline_markup=InlineMarkup([[
            InlineKeyboardButton("Open Travel Planner", callback_data="main_menu", app=True)
        ]])
    )

@app.on_callback_query(regexp("main_menu"))
async def main_menu(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Travel Planner", size=TextSize.LARGE),
            ButtonGroup([
                Button("Explore Destinations", callback_data="explore_destinations"),
                Button("Weather Forecast", callback_data="weather_forecast"),
                Button("Currency Converter", callback_data="currency_converter"),
                Button("My Itinerary", callback_data="view_itinerary"),
            ]),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("explore_destinations"))
async def explore_destinations(ctx: BotContext[CallbackQueryEvent]):
    destination_items = [
        GridItem(
            f"{dest['name']}, {dest['country']}",
            dest['image'],
            callback_data=f"destination_{key}"
        ) for key, dest in destinations.items()
    ]
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Explore Destinations", size=TextSize.LARGE),
            Grid(title="Popular Destinations", options=destination_items),
            Button("Back to Main Menu", callback_data="main_menu"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("destination_"))
async def show_destination(ctx: BotContext[CallbackQueryEvent]):
    dest_key = ctx.event.callback_data.split("_")[1]
    dest = destinations[dest_key]
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text(f"{dest['name']}, {dest['country']}", size=TextSize.LARGE),
            Image(dest['image']),
            Text(dest['description'], size=TextSize.MEDIUM),
            VideoPlayer(dest['video'], title=f"Discover {dest['name']}"),
            ButtonGroup([
                Button("Add to Itinerary", callback_data=f"add_to_itinerary_{dest_key}"),
                Button("Back to Destinations", callback_data="explore_destinations"),
            ]),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("weather_forecast"))
async def weather_forecast(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Weather Forecast", size=TextSize.LARGE),
            Text("Enter a city name:"),
            SearchBar(callback_data="get_weather"),
            Button("Back to Main Menu", callback_data="main_menu"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("get_weather"))
async def get_weather(ctx: BotContext[CallbackQueryEvent]):
    city = ctx.event.details.get("searchQuery", "").strip()
    if not city:
        await ctx.event.answer("Please enter a city name.", show_alert=True)
        return
    
    async with aiohttp.ClientSession() as session:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric"
        async with session.get(url) as response:
            data = await response.json()
    
    if data["cod"] != "200":
        await ctx.event.answer(f"Error: {data['message']}", show_alert=True)
        return
    
    forecast = data["list"][:5]  # Get forecast for the next 5 time slots
    forecast_items = [
        ListItem(
            f"{datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M')}: "
            f"{item['main']['temp']}°C, {item['weather'][0]['description']}",
            callback_data=f"weather_details_{item['dt']}"
        ) for item in forecast
    ]
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text(f"Weather Forecast for {city}", size=TextSize.LARGE),
            Dropdown("Select a time for details", options=forecast_items),
            Button("Back to Weather Search", callback_data="weather_forecast"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("currency_converter"))
async def currency_converter(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Currency Converter", size=TextSize.LARGE),
            Text("Enter amount and currency codes (e.g., 100 USD to EUR):"),
            SearchBar(callback_data="convert_currency"),
            Button("Back to Main Menu", callback_data="main_menu"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("convert_currency"))
async def convert_currency(ctx: BotContext[CallbackQueryEvent]):
    query = ctx.event.details.get("searchQuery", "").strip().upper()
    try:
        amount, from_currency, _, to_currency = query.split()
        amount = float(amount)
    except ValueError:
        await ctx.event.answer("Invalid input. Please use format: 100 USD to EUR", show_alert=True)
        return
    
    async with aiohttp.ClientSession() as session:
        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/{from_currency}"
        async with session.get(url) as response:
            data = await response.json()
    
    if data["result"] != "success":
        await ctx.event.answer(f"Error: {data['error-type']}", show_alert=True)
        return
    
    rate = data["conversion_rates"].get(to_currency)
    if not rate:
        await ctx.event.answer(f"Error: Could not find conversion rate for {to_currency}", show_alert=True)
        return
    
    converted_amount = amount * rate
    result = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Currency Conversion Result", size=TextSize.LARGE),
            Text(result, size=TextSize.MEDIUM),
            Button("Convert Another Amount", callback_data="currency_converter"),
            Button("Back to Main Menu", callback_data="main_menu"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("add_to_itinerary_"))
async def add_to_itinerary(ctx: BotContext[CallbackQueryEvent]):
    dest_key = ctx.event.callback_data.split("_")[-1]
    user_id = ctx.event.action_by_id
    
    if user_id not in user_itineraries:
        user_itineraries[user_id] = []
    
    user_itineraries[user_id].append(destinations[dest_key])
    await ctx.event.answer(f"{destinations[dest_key]['name']} added to your itinerary!", show_alert=True)

@app.on_callback_query(regexp("view_itinerary"))
async def view_itinerary(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    itinerary = user_itineraries.get(user_id, [])
    
    if not itinerary:
        await ctx.event.answer("Your itinerary is empty. Start by adding some destinations!", show_alert=True)
        return
    
    itinerary_items = [
        EmbeddedMedia(
            thumbnail=dest['image'],
            title=f"{dest['name']}, {dest['country']}",
            description=dest['description'],
        ) for dest in itinerary
    ]
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Your Travel Itinerary", size=TextSize.LARGE),
            Carousel(itinerary_items),
            Button("Back to Main Menu", callback_data="main_menu"),
        ]
    )
    await ctx.event.answer(callback=page)

if __name__ == "__main__":
    app.run()
```

## Features Demonstrated

This example showcases the following SwiBots features:

1. Creating a complex mini app with multiple interconnected features
2. Using a wide variety of UI components:
   - Text
   - Buttons and ButtonGroups
   - Grid and GridItems
   - Image
   - VideoPlayer
   - SearchBar
   - Dropdown
   - ListItem
   - EmbeddedMedia