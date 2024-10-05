# Task Management Bot Example

This example demonstrates a real-world use case of a mini app using SwiBots. The bot creates a task management application where users can add tasks, mark them as complete, and view their task lists.

## Prerequisites

Before you begin, make sure you have:

1. Installed SwiBots (`pip install swibots`)
2. Obtained a bot token from the Switch platform

## The Code

Here's the complete code for our task management bot:

```python
import logging
from swibots import (
    Client, BotContext, CommandEvent, CallbackQueryEvent, BotCommand,
    AppPage, Text, Button, ButtonGroup, Grid, GridItem,
    ScreenType, TextSize, InlineKeyboardButton, InlineMarkup
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_BOT_TOKEN_HERE"

app = Client(TOKEN, is_app=True, home_callback="show_tasks")
app.set_bot_commands([BotCommand("start", "Open the task manager", True)])

# In-memory storage for tasks (in a real application, you'd use a database)
user_tasks = {}

@app.on_command("start")
async def start_command(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(
        "Welcome to your Task Manager! Click the button below to view your tasks.",
        inline_markup=InlineMarkup([[
            InlineKeyboardButton("Open Task Manager", callback_data="show_tasks", app=True)
        ]])
    )

@app.on_callback_query(regexp("show_tasks"))
async def show_tasks(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    tasks = user_tasks.get(user_id, [])
    
    task_items = [
        GridItem(f"{task['title']}\n{'✅' if task['completed'] else '❌'}", 
                 "https://example.com/task-icon.png",
                 callback_data=f"toggle_task_{i}")
        for i, task in enumerate(tasks)
    ]
    
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Your Tasks", size=TextSize.LARGE),
            Grid(title="Task List", options=task_items) if tasks else Text("No tasks yet. Add some tasks!"),
            ButtonGroup([
                Button("Add Task", callback_data="add_task"),
                Button("Clear Completed", callback_data="clear_completed"),
            ]),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("add_task"))
async def add_task(ctx: BotContext[CallbackQueryEvent]):
    page = AppPage(
        screen=ScreenType.SCREEN,
        components=[
            Text("Add a New Task", size=TextSize.LARGE),
            Text("Enter your task title:"),
            Button("Submit", callback_data="submit_task"),
        ]
    )
    await ctx.event.answer(callback=page)

@app.on_callback_query(regexp("submit_task"))
async def submit_task(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    task_title = ctx.event.details.get("searchQuery", "").strip()
    
    if task_title:
        if user_id not in user_tasks:
            user_tasks[user_id] = []
        user_tasks[user_id].append({"title": task_title, "completed": False})
        await ctx.event.answer("Task added successfully!", show_alert=True)
    else:
        await ctx.event.answer("Please enter a task title.", show_alert=True)
    
    await show_tasks(ctx)

@app.on_callback_query(regexp("toggle_task_"))
async def toggle_task(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    task_index = int(ctx.event.callback_data.split("_")[-1])
    
    if user_id in user_tasks and 0 <= task_index < len(user_tasks[user_id]):
        user_tasks[user_id][task_index]["completed"] = not user_tasks[user_id][task_index]["completed"]
        status = "completed" if user_tasks[user_id][task_index]["completed"] else "uncompleted"
        await ctx.event.answer(f"Task marked as {status}!", show_alert=True)
    else:
        await ctx.event.answer("Invalid task.", show_alert=True)
    
    await show_tasks(ctx)

@app.on_callback_query(regexp("clear_completed"))
async def clear_completed(ctx: BotContext[CallbackQueryEvent]):
    user_id = ctx.event.action_by_id
    if user_id in user_tasks:
        user_tasks[user_id] = [task for task in user_tasks[user_id] if not task["completed"]]
        await ctx.event.answer("Completed tasks cleared!", show_alert=True)
    else:
        await ctx.event.answer("No tasks to clear.", show_alert=True)
    
    await show_tasks(ctx)

if __name__ == "__main__":
    app.run()
```

## Features Demonstrated

This example showcases the following SwiBots features:

1. Creating a mini app for a practical task management use case
2. Using various UI components:
   - Text
   - Buttons and ButtonGroups
   - Grid and GridItems
3. Implementing navigation between different screens
4. Maintaining user state (tasks) across interactions
5. Handling user actions like adding tasks, toggling task status, and clearing completed tasks

## How It Works

1. The bot starts with a welcome message and a button to open the task manager.
2. The main screen shows a list of tasks (if any) and options to add tasks or clear completed tasks.
3. Users can add new tasks, which are then displayed in the task list.
4. Tasks can be toggled between completed and uncompleted states by clicking on them.
5. Completed tasks can be cleared from the list using the "Clear Completed" button.

This example demonstrates how to create an interactive mini app that could be used for personal task management or integrated into a larger productivity suite.

## Running the Bot

To run the bot, save the complete code in a file (e.g., `task_management_bot.py`) and execute it:

```bash
python task_management_bot.py
```

## Note

This is a simplified implementation for demonstration purposes. In a production environment, you would need to add error handling, integrate with a persistent database for storing tasks, implement user authentication, and add more features like task categories, due dates, and reminders.