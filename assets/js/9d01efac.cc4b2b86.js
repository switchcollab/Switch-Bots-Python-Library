"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[7204],{8487:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>c,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>a,toc:()=>l});const a=JSON.parse('{"id":"examples/restaurant-menu-bot","title":"Restaurant Menu and Order Bot Example","description":"This example demonstrates a real-world use case of a mini app using SwiBots. The bot creates a restaurant menu app where users can browse menu items, add them to a cart, and place an order.","source":"@site/docs/examples/restaurant-menu-bot.md","sourceDirName":"examples","slug":"/examples/restaurant-menu-bot","permalink":"/Switch-Bots-Python-Library/docs/examples/restaurant-menu-bot","draft":false,"unlisted":false,"tags":[],"version":"current","frontMatter":{},"sidebar":"tutorialSidebar","previous":{"title":"Poll Bot Example","permalink":"/Switch-Bots-Python-Library/docs/examples/poll-bot"},"next":{"title":"Task Management Bot Example","permalink":"/Switch-Bots-Python-Library/docs/examples/task-management-bot"}}');var r=t(4848),s=t(8453);const i={},o="Restaurant Menu and Order Bot Example",c={},l=[{value:"Prerequisites",id:"prerequisites",level:2},{value:"The Code",id:"the-code",level:2},{value:"Features Demonstrated",id:"features-demonstrated",level:2},{value:"How It Works",id:"how-it-works",level:2},{value:"Running the Bot",id:"running-the-bot",level:2},{value:"Note",id:"note",level:2}];function d(e){const n={code:"code",h1:"h1",h2:"h2",header:"header",li:"li",ol:"ol",p:"p",pre:"pre",ul:"ul",...(0,s.R)(),...e.components};return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(n.header,{children:(0,r.jsx)(n.h1,{id:"restaurant-menu-and-order-bot-example",children:"Restaurant Menu and Order Bot Example"})}),"\n",(0,r.jsx)(n.p,{children:"This example demonstrates a real-world use case of a mini app using SwiBots. The bot creates a restaurant menu app where users can browse menu items, add them to a cart, and place an order."}),"\n",(0,r.jsx)(n.h2,{id:"prerequisites",children:"Prerequisites"}),"\n",(0,r.jsx)(n.p,{children:"Before you begin, make sure you have:"}),"\n",(0,r.jsxs)(n.ol,{children:["\n",(0,r.jsxs)(n.li,{children:["Installed SwiBots (",(0,r.jsx)(n.code,{children:"pip install swibots"}),")"]}),"\n",(0,r.jsx)(n.li,{children:"Obtained a bot token from the Switch platform"}),"\n"]}),"\n",(0,r.jsx)(n.h2,{id:"the-code",children:"The Code"}),"\n",(0,r.jsx)(n.p,{children:"Here's the complete code for our restaurant menu bot:"}),"\n",(0,r.jsx)(n.pre,{children:(0,r.jsx)(n.code,{className:"language-python",children:'import logging\nfrom swibots import (\n    Client, BotContext, CommandEvent, CallbackQueryEvent, BotCommand,\n    AppPage, Text, Button, ButtonGroup, Image, Grid, GridItem,\n    ScreenType, TextSize, InlineKeyboardButton, InlineMarkup, regexp\n)\n\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\n\nTOKEN = "YOUR_BOT_TOKEN_HERE"\n\napp = Client(TOKEN, is_app=True, home_callback="show_menu")\napp.set_bot_commands([BotCommand("start", "Open the restaurant menu", True)])\n\n# Simulated menu data\nmenu = {\n    "appetizers": [\n        {"id": "app1", "name": "Bruschetta", "price": 7.99, "image": "https://example.com/bruschetta.jpg"},\n        {"id": "app2", "name": "Mozzarella Sticks", "price": 6.99, "image": "https://example.com/mozzarella.jpg"},\n    ],\n    "main_courses": [\n        {"id": "main1", "name": "Spaghetti Carbonara", "price": 14.99, "image": "https://example.com/carbonara.jpg"},\n        {"id": "main2", "name": "Grilled Salmon", "price": 18.99, "image": "https://example.com/salmon.jpg"},\n    ],\n    "desserts": [\n        {"id": "des1", "name": "Tiramisu", "price": 6.99, "image": "https://example.com/tiramisu.jpg"},\n        {"id": "des2", "name": "Cheesecake", "price": 5.99, "image": "https://example.com/cheesecake.jpg"},\n    ]\n}\n\n# User cart\nuser_carts = {}\n\n@app.on_command("start")\nasync def start_command(ctx: BotContext[CommandEvent]):\n    await ctx.event.message.reply_text(\n        "Welcome to our restaurant! Click the button below to see our menu.",\n        inline_markup=InlineMarkup([[\n            InlineKeyboardButton("View Menu", callback_data="show_menu", app=True)\n        ]])\n    )\n\n@app.on_callback_query(regexp("show_menu"))\nasync def show_menu(ctx: BotContext[CallbackQueryEvent]):\n    page = AppPage(\n        screen=ScreenType.SCREEN,\n        components=[\n            Text("Our Menu", size=TextSize.LARGE),\n            ButtonGroup([\n                Button("Appetizers", callback_data="menu_appetizers"),\n                Button("Main Courses", callback_data="menu_main_courses"),\n                Button("Desserts", callback_data="menu_desserts"),\n            ]),\n            Button("View Cart", callback_data="view_cart"),\n        ]\n    )\n    await ctx.event.answer(callback=page)\n\n@app.on_callback_query(regexp("menu_"))\nasync def show_category(ctx: BotContext[CallbackQueryEvent]):\n    category = ctx.event.callback_data.split("_")[1]\n    items = menu[category]\n    \n    page = AppPage(\n        screen=ScreenType.SCREEN,\n        components=[\n            Text(f"{category.capitalize()}", size=TextSize.LARGE),\n            Grid(\n                title="Menu Items",\n                options=[\n                    GridItem(\n                        f"{item[\'name\']}\\n${item[\'price\']:.2f}",\n                        item[\'image\'],\n                        callback_data=f"add_to_cart_{item[\'id\']}"\n                    ) for item in items\n                ]\n            ),\n            Button("Back to Menu", callback_data="show_menu"),\n        ]\n    )\n    await ctx.event.answer(callback=page)\n\n@app.on_callback_query(regexp("add_to_cart_"))\nasync def add_to_cart(ctx: BotContext[CallbackQueryEvent]):\n    item_id = ctx.event.callback_data.split("_")[-1]\n    user_id = ctx.event.action_by_id\n    \n    if user_id not in user_carts:\n        user_carts[user_id] = {}\n    \n    if item_id in user_carts[user_id]:\n        user_carts[user_id][item_id] += 1\n    else:\n        user_carts[user_id][item_id] = 1\n    \n    await ctx.event.answer("Item added to cart!", show_alert=True)\n\n@app.on_callback_query(regexp("view_cart"))\nasync def view_cart(ctx: BotContext[CallbackQueryEvent]):\n    user_id = ctx.event.action_by_id\n    cart = user_carts.get(user_id, {})\n    \n    if not cart:\n        await ctx.event.answer("Your cart is empty!", show_alert=True)\n        return\n    \n    total = 0\n    cart_items = []\n    for item_id, quantity in cart.items():\n        item = next(item for category in menu.values() for item in category if item[\'id\'] == item_id)\n        subtotal = item[\'price\'] * quantity\n        total += subtotal\n        cart_items.append(f"{item[\'name\']} x{quantity}: ${subtotal:.2f}")\n    \n    page = AppPage(\n        screen=ScreenType.SCREEN,\n        components=[\n            Text("Your Cart", size=TextSize.LARGE),\n            Text("\\n".join(cart_items), size=TextSize.MEDIUM),\n            Text(f"Total: ${total:.2f}", size=TextSize.LARGE),\n            ButtonGroup([\n                Button("Place Order", callback_data="place_order"),\n                Button("Back to Menu", callback_data="show_menu"),\n            ]),\n        ]\n    )\n    await ctx.event.answer(callback=page)\n\n@app.on_callback_query(regexp("place_order"))\nasync def place_order(ctx: BotContext[CallbackQueryEvent]):\n    user_id = ctx.event.action_by_id\n    if user_id in user_carts:\n        del user_carts[user_id]\n        await ctx.event.answer("Your order has been placed! Thank you for your purchase.", show_alert=True)\n    else:\n        await ctx.event.answer("Your cart is empty!", show_alert=True)\n\nif __name__ == "__main__":\n    app.run()\n'})}),"\n",(0,r.jsx)(n.h2,{id:"features-demonstrated",children:"Features Demonstrated"}),"\n",(0,r.jsx)(n.p,{children:"This example showcases the following SwiBots features:"}),"\n",(0,r.jsxs)(n.ol,{children:["\n",(0,r.jsx)(n.li,{children:"Creating a mini app with a practical, real-world use case"}),"\n",(0,r.jsxs)(n.li,{children:["Using various UI components:","\n",(0,r.jsxs)(n.ul,{children:["\n",(0,r.jsx)(n.li,{children:"Text"}),"\n",(0,r.jsx)(n.li,{children:"Buttons and ButtonGroups"}),"\n",(0,r.jsx)(n.li,{children:"Grid and GridItems"}),"\n"]}),"\n"]}),"\n",(0,r.jsx)(n.li,{children:"Implementing navigation between different screens"}),"\n",(0,r.jsx)(n.li,{children:"Maintaining user state (shopping cart) across interactions"}),"\n",(0,r.jsx)(n.li,{children:"Handling user actions like adding items to cart and placing orders"}),"\n"]}),"\n",(0,r.jsx)(n.h2,{id:"how-it-works",children:"How It Works"}),"\n",(0,r.jsxs)(n.ol,{children:["\n",(0,r.jsx)(n.li,{children:"The bot starts with a welcome message and a button to view the menu."}),"\n",(0,r.jsx)(n.li,{children:'The main menu screen shows categories (Appetizers, Main Courses, Desserts) and a "View Cart" button.'}),"\n",(0,r.jsx)(n.li,{children:"Each category screen displays menu items in a grid, allowing users to add items to their cart."}),"\n",(0,r.jsx)(n.li,{children:"The cart screen shows the selected items, quantities, and total price, with options to place the order or return to the menu."}),"\n",(0,r.jsx)(n.li,{children:"When an order is placed, the cart is cleared, and a confirmation message is shown."}),"\n"]}),"\n",(0,r.jsx)(n.p,{children:"This example demonstrates how to create a more complex, interactive mini app that could be used by real businesses to showcase their products and handle customer orders."}),"\n",(0,r.jsx)(n.h2,{id:"running-the-bot",children:"Running the Bot"}),"\n",(0,r.jsxs)(n.p,{children:["To run the bot, save the complete code in a file (e.g., ",(0,r.jsx)(n.code,{children:"restaurant_menu_bot.py"}),") and execute it:"]}),"\n",(0,r.jsx)(n.pre,{children:(0,r.jsx)(n.code,{className:"language-bash",children:"python restaurant_menu_bot.py\n"})}),"\n",(0,r.jsx)(n.h2,{id:"note",children:"Note"}),"\n",(0,r.jsx)(n.p,{children:"This is a simplified implementation for demonstration purposes. In a production environment, you would need to add error handling, integrate with a real database for menu items and orders, implement user authentication, and add more features like order tracking and payment processing."})]})}function u(e={}){const{wrapper:n}={...(0,s.R)(),...e.components};return n?(0,r.jsx)(n,{...e,children:(0,r.jsx)(d,{...e})}):d(e)}},8453:(e,n,t)=>{t.d(n,{R:()=>i,x:()=>o});var a=t(6540);const r={},s=a.createContext(r);function i(e){const n=a.useContext(s);return a.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function o(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:i(e.components),a.createElement(s.Provider,{value:n},e.children)}}}]);