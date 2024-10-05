# Calculator Bot Example

This example demonstrates a more complex use case of a mini app using SwiBots. The bot creates an advanced calculator with basic arithmetic, scientific functions, and calculation history.

## Prerequisites

Before you begin, make sure you have:

1. Installed SwiBots (`pip install swibots`)
2. Obtained a bot token from the Switch platform
3. Installed the `math` module (usually comes pre-installed with Python)

## The Code

Here's the complete code for our advanced calculator bot:

```python
import logging
import math
from swibots import (
    Client, BotContext, CommandEvent, CallbackQueryEvent, BotCommand,
    AppPage, Text, Button, ButtonGroup,
    ScreenType, TextSize, InlineKeyboardButton, InlineMarkup, regexp
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_BOT_TOKEN_HERE"

app = Client(TOKEN, is_app=True, home_callback="show_calculator")
app.set_bot_commands([BotCommand("start", "Open the calculator", True)])

# Store calculation history
user_history = {}

def evaluate_expression(expression):
    try:
        # Replace '^' with '**' for exponentiation
        expression = expression.replace('^', '**')
        # Add math. prefix to mathematical functions
        for func in ['sin', 'cos', 'tan', 'log', 'sqrt']:
            expression = expression.replace(func, f'math.{func}')
        return str(eval(expression, {"__builtins__": None}, {"math": math}))
    except Exception as e:
        return f"Error: {str(e)}"

@app.on_command("start")
async def start_command(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(
        "Welcome to the Advanced Calculator! Click the button below to start calculating.",
        inline_markup=InlineMarkup([[
            InlineKeyboardButton("Open Calculator", callback_data="show_calculator", app=True)
        ]])
    )

@app.on_callback_query(regexp("show_calculator"))
async def show_calculator(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    current_expression = user_history.get(user_id, {}).get('current', '')
    
    calculator_buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["(", ")", "C", "←"],
        ["sin", "cos", "tan", "^"],
        ["log", "sqrt", "π", "e"],
    ]
    
    button_groups = [
        ButtonGroup([Button(btn, callback_data=f"calc_{btn}") for btn in row])
        for row in calculator_buttons
    ]
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Advanced Calculator", size=TextSize.LARGE),
            Text(current_expression or "0", size=TextSize.MEDIUM),
            *button_groups,
            Button("View History", callback_data="view_history"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("calc_"))
async def handle_calculation(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    button = ctx.event.callback_data.split("_")[1]
    
    if user_id not in user_history:
        user_history[user_id] = {'current': '', 'history': []}
    
    current = user_history[user_id]['current']
    
    if button == "=":
        result = evaluate_expression(current)
        user_history[user_id]['history'].append(f"{current} = {result}")
        user_history[user_id]['current'] = result
    elif button == "C":
        user_history[user_id]['current'] = ''
    elif button == "←":
        user_history[user_id]['current'] = current[:-1]
    elif button == "π":
        user_history[user_id]['current'] += str(math.pi)
    elif button == "e":
        user_history[user_id]['current'] += str(math.e)
    else:
        user_history[user_id]['current'] += button
    
    await show_calculator(ctx)

@app.on_callback_query(regexp("view_history"))
async def view_history(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    history = user_history.get(user_id, {}).get('history', [])
    
    if not history:
        await ctx.event.answer("No calculation history available.", show_alert=True)
        return
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Calculation History", size=TextSize.LARGE),
            Text("\n".join(history[-10:]), size=TextSize.MEDIUM),
            Button("Back to Calculator", callback_data="show_calculator"),
        ]
    )
    await ctx.event.answer(callback=page)

if __name__ == "__main__":
    app.run()
```

## Features Demonstrated

This example showcases the following SwiBots features:

1. Creating a complex mini app with advanced functionality
2. Using various UI components:
   - Text
   - Buttons and ButtonGroups
3. Implementing a calculator interface with multiple operations
4. Maintaining user state (current expression and calculation history)
5. Handling user actions for various calculator functions
6. Integrating with Python's `math` module for advanced calculations

## How It Works

1. The bot starts with a welcome message and a button to open the calculator.
2. The main calculator screen shows the current expression and buttons for various operations.
3. Users can input numbers and perform various operations, including basic arithmetic and scientific functions.
4. The calculator evaluates expressions and displays results.
5. Users can view their calculation history.

This example demonstrates how to create a more complex, interactive mini app that provides practical functionality while showcasing various SwiBots features.

## Running the Bot

To run the bot, save the complete code in a file (e.g., `advanced_calculator_bot.py`) and execute it:

```bash
python advanced_calculator_bot.py
```

## Note

This implementation uses Python's `eval()` function, which can be dangerous if used with untrusted input. In a production environment, you should implement a safer method of evaluating mathematical expressions, such as using a parsing library or implementing your own expression evaluator.