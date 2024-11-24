"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[3167],{33:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>o,default:()=>u,frontMatter:()=>r,metadata:()=>a,toc:()=>d});const a=JSON.parse('{"id":"examples/task-management-bot","title":"Task Management Bot Example","description":"This example demonstrates a real-world use case of a mini app using SwiBots. The bot creates a task management application where users can add tasks, mark them as complete, and view their task lists.","source":"@site/docs/examples/task-management-bot.md","sourceDirName":"examples","slug":"/examples/task-management-bot","permalink":"/Switch-Bots-Python-Library/docs/examples/task-management-bot","draft":false,"unlisted":false,"tags":[],"version":"current","frontMatter":{},"sidebar":"tutorialSidebar","previous":{"title":"Restaurant Menu and Order Bot Example","permalink":"/Switch-Bots-Python-Library/docs/examples/restaurant-menu-bot"},"next":{"title":"Travel Planner Bot Example","permalink":"/Switch-Bots-Python-Library/docs/examples/travel-planner-bot"}}');var s=n(4848),i=n(8453);const r={},o="Task Management Bot Example",l={},d=[{value:"Prerequisites",id:"prerequisites",level:2},{value:"The Code",id:"the-code",level:2},{value:"Features Demonstrated",id:"features-demonstrated",level:2},{value:"How It Works",id:"how-it-works",level:2},{value:"Running the Bot",id:"running-the-bot",level:2},{value:"Note",id:"note",level:2}];function c(e){const t={code:"code",h1:"h1",h2:"h2",header:"header",li:"li",ol:"ol",p:"p",pre:"pre",ul:"ul",...(0,i.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(t.header,{children:(0,s.jsx)(t.h1,{id:"task-management-bot-example",children:"Task Management Bot Example"})}),"\n",(0,s.jsx)(t.p,{children:"This example demonstrates a real-world use case of a mini app using SwiBots. The bot creates a task management application where users can add tasks, mark them as complete, and view their task lists."}),"\n",(0,s.jsx)(t.h2,{id:"prerequisites",children:"Prerequisites"}),"\n",(0,s.jsx)(t.p,{children:"Before you begin, make sure you have:"}),"\n",(0,s.jsxs)(t.ol,{children:["\n",(0,s.jsxs)(t.li,{children:["Installed SwiBots (",(0,s.jsx)(t.code,{children:"pip install swibots"}),")"]}),"\n",(0,s.jsx)(t.li,{children:"Obtained a bot token from the Switch platform"}),"\n"]}),"\n",(0,s.jsx)(t.h2,{id:"the-code",children:"The Code"}),"\n",(0,s.jsx)(t.p,{children:"Here's the complete code for our task management bot:"}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",children:'import logging\nfrom swibots import (\n    Client, BotContext, CommandEvent, CallbackQueryEvent, BotCommand,\n    AppPage, Text, Button, ButtonGroup, Grid, GridItem,\n    ScreenType, TextSize, InlineKeyboardButton, InlineMarkup\n)\n\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\n\nTOKEN = "YOUR_BOT_TOKEN_HERE"\n\napp = Client(TOKEN, is_app=True, home_callback="show_tasks")\napp.set_bot_commands([BotCommand("start", "Open the task manager", True)])\n\n# In-memory storage for tasks (in a real application, you\'d use a database)\nuser_tasks = {}\n\n@app.on_command("start")\nasync def start_command(ctx: BotContext[CommandEvent]):\n    await ctx.event.message.reply_text(\n        "Welcome to your Task Manager! Click the button below to view your tasks.",\n        inline_markup=InlineMarkup([[\n            InlineKeyboardButton("Open Task Manager", callback_data="show_tasks", app=True)\n        ]])\n    )\n\n@app.on_callback_query(regexp("show_tasks"))\nasync def show_tasks(ctx: BotContext[CallbackQueryEvent]):\n    user_id = ctx.event.action_by_id\n    tasks = user_tasks.get(user_id, [])\n    \n    task_items = [\n        GridItem(f"{task[\'title\']}\\n{\'\u2705\' if task[\'completed\'] else \'\u274c\'}", \n                 "https://example.com/task-icon.png",\n                 callback_data=f"toggle_task_{i}")\n        for i, task in enumerate(tasks)\n    ]\n    \n    page = AppPage(\n        screen=ScreenType.SCREEN,\n        components=[\n            Text("Your Tasks", size=TextSize.LARGE),\n            Grid(title="Task List", options=task_items) if tasks else Text("No tasks yet. Add some tasks!"),\n            ButtonGroup([\n                Button("Add Task", callback_data="add_task"),\n                Button("Clear Completed", callback_data="clear_completed"),\n            ]),\n        ]\n    )\n    await ctx.event.answer(callback=page)\n\n@app.on_callback_query(regexp("add_task"))\nasync def add_task(ctx: BotContext[CallbackQueryEvent]):\n    page = AppPage(\n        screen=ScreenType.SCREEN,\n        components=[\n            Text("Add a New Task", size=TextSize.LARGE),\n            Text("Enter your task title:"),\n            Button("Submit", callback_data="submit_task"),\n        ]\n    )\n    await ctx.event.answer(callback=page)\n\n@app.on_callback_query(regexp("submit_task"))\nasync def submit_task(ctx: BotContext[CallbackQueryEvent]):\n    user_id = ctx.event.action_by_id\n    task_title = ctx.event.details.get("searchQuery", "").strip()\n    \n    if task_title:\n        if user_id not in user_tasks:\n            user_tasks[user_id] = []\n        user_tasks[user_id].append({"title": task_title, "completed": False})\n        await ctx.event.answer("Task added successfully!", show_alert=True)\n    else:\n        await ctx.event.answer("Please enter a task title.", show_alert=True)\n    \n    await show_tasks(ctx)\n\n@app.on_callback_query(regexp("toggle_task_"))\nasync def toggle_task(ctx: BotContext[CallbackQueryEvent]):\n    user_id = ctx.event.action_by_id\n    task_index = int(ctx.event.callback_data.split("_")[-1])\n    \n    if user_id in user_tasks and 0 <= task_index < len(user_tasks[user_id]):\n        user_tasks[user_id][task_index]["completed"] = not user_tasks[user_id][task_index]["completed"]\n        status = "completed" if user_tasks[user_id][task_index]["completed"] else "uncompleted"\n        await ctx.event.answer(f"Task marked as {status}!", show_alert=True)\n    else:\n        await ctx.event.answer("Invalid task.", show_alert=True)\n    \n    await show_tasks(ctx)\n\n@app.on_callback_query(regexp("clear_completed"))\nasync def clear_completed(ctx: BotContext[CallbackQueryEvent]):\n    user_id = ctx.event.action_by_id\n    if user_id in user_tasks:\n        user_tasks[user_id] = [task for task in user_tasks[user_id] if not task["completed"]]\n        await ctx.event.answer("Completed tasks cleared!", show_alert=True)\n    else:\n        await ctx.event.answer("No tasks to clear.", show_alert=True)\n    \n    await show_tasks(ctx)\n\nif __name__ == "__main__":\n    app.run()\n'})}),"\n",(0,s.jsx)(t.h2,{id:"features-demonstrated",children:"Features Demonstrated"}),"\n",(0,s.jsx)(t.p,{children:"This example showcases the following SwiBots features:"}),"\n",(0,s.jsxs)(t.ol,{children:["\n",(0,s.jsx)(t.li,{children:"Creating a mini app for a practical task management use case"}),"\n",(0,s.jsxs)(t.li,{children:["Using various UI components:","\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsx)(t.li,{children:"Text"}),"\n",(0,s.jsx)(t.li,{children:"Buttons and ButtonGroups"}),"\n",(0,s.jsx)(t.li,{children:"Grid and GridItems"}),"\n"]}),"\n"]}),"\n",(0,s.jsx)(t.li,{children:"Implementing navigation between different screens"}),"\n",(0,s.jsx)(t.li,{children:"Maintaining user state (tasks) across interactions"}),"\n",(0,s.jsx)(t.li,{children:"Handling user actions like adding tasks, toggling task status, and clearing completed tasks"}),"\n"]}),"\n",(0,s.jsx)(t.h2,{id:"how-it-works",children:"How It Works"}),"\n",(0,s.jsxs)(t.ol,{children:["\n",(0,s.jsx)(t.li,{children:"The bot starts with a welcome message and a button to open the task manager."}),"\n",(0,s.jsx)(t.li,{children:"The main screen shows a list of tasks (if any) and options to add tasks or clear completed tasks."}),"\n",(0,s.jsx)(t.li,{children:"Users can add new tasks, which are then displayed in the task list."}),"\n",(0,s.jsx)(t.li,{children:"Tasks can be toggled between completed and uncompleted states by clicking on them."}),"\n",(0,s.jsx)(t.li,{children:'Completed tasks can be cleared from the list using the "Clear Completed" button.'}),"\n"]}),"\n",(0,s.jsx)(t.p,{children:"This example demonstrates how to create an interactive mini app that could be used for personal task management or integrated into a larger productivity suite."}),"\n",(0,s.jsx)(t.h2,{id:"running-the-bot",children:"Running the Bot"}),"\n",(0,s.jsxs)(t.p,{children:["To run the bot, save the complete code in a file (e.g., ",(0,s.jsx)(t.code,{children:"task_management_bot.py"}),") and execute it:"]}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-bash",children:"python task_management_bot.py\n"})}),"\n",(0,s.jsx)(t.h2,{id:"note",children:"Note"}),"\n",(0,s.jsx)(t.p,{children:"This is a simplified implementation for demonstration purposes. In a production environment, you would need to add error handling, integrate with a persistent database for storing tasks, implement user authentication, and add more features like task categories, due dates, and reminders."})]})}function u(e={}){const{wrapper:t}={...(0,i.R)(),...e.components};return t?(0,s.jsx)(t,{...e,children:(0,s.jsx)(c,{...e})}):c(e)}},8453:(e,t,n)=>{n.d(t,{R:()=>r,x:()=>o});var a=n(6540);const s={},i=a.createContext(s);function r(e){const t=a.useContext(i);return a.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function o(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(s):e.components||s:r(e.components),a.createElement(i.Provider,{value:t},e.children)}}}]);