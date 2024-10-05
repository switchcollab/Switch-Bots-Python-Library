# Weather Bot Example

This example demonstrates how to create a weather bot using SwiBots. The bot can fetch current weather information for a given city using the OpenWeatherMap API.

## Prerequisites

Before you begin, make sure you have:

1. Installed SwiBots (`pip install swibots`)
2. Installed the `requests` library (`pip install requests`)
3. Obtained a bot token from the Switch platform
4. Signed up for a free API key from [OpenWeatherMap](https://openweathermap.org/api)

## The Code

Here's the complete code for our weather bot:

```python
import os
from swibots import Client, BotContext, MessageEvent
import requests

app = Client(os.environ["BOT_TOKEN"])
WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]

@app.on_message()
async def weather_handler(ctx: BotContext[MessageEvent]):
    message = ctx.event.message
    if message.message.startswith("/weather"):
        city = message.message.split("/weather ", 1)[1]
        weather_data = get_weather(city)
        if weather_data:
            response = format_weather_response(city, weather_data)
        else:
            response = f"Sorry, I couldn't find weather information for {city}."
        await message.respond(response)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def format_weather_response(city, data):
    main = data['main']
    weather = data['weather'][0]
    return f"""Weather in {city}:
Temperature: {main['temp']}°C
Feels like: {main['feels_like']}°C
Humidity: {main['humidity']}%
Description: {weather['description'].capitalize()}"""

app.run()
```

## Running the Bot

To run the bot, set your environment variables and execute the script:

```bash
export BOT_TOKEN="your_bot_token_here"
export WEATHER_API_KEY="your_openweathermap_api_key_here"
python weather_bot.py
```

## Using the Bot

To use the bot, send a message in the following format:

```
/weather City Name
```

For example:
```
/weather London
```

The bot will respond with current weather information for the specified city.

## Note

This is a basic implementation. You might want to add error handling, input validation, and more features to make it production-ready.