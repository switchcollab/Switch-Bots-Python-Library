"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[6137],{398:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>c,contentTitle:()=>s,default:()=>h,frontMatter:()=>a,metadata:()=>d,toc:()=>i});var r=t(4848),o=t(8453);const a={sidebar_position:4},s="Decorator Handlers",d={id:"fundamentals/decorators",title:"Decorator Handlers",description:"If you don't want to use the add_handler method, you can use decorators to register handlers to the app.",source:"@site/docs/fundamentals/decorators.md",sourceDirName:"fundamentals",slug:"/fundamentals/decorators",permalink:"/Switch-Bots-Python-Library/docs/fundamentals/decorators",draft:!1,unlisted:!1,tags:[],version:"current",sidebarPosition:4,frontMatter:{sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Handlers",permalink:"/Switch-Bots-Python-Library/docs/fundamentals/handlers"},next:{title:"Bot Context",permalink:"/Switch-Bots-Python-Library/docs/fundamentals/context"}},c={},i=[{value:"Decorators",id:"decorators",level:2},{value:"Example",id:"example",level:3}];function l(e){const n={a:"a",code:"code",h1:"h1",h2:"h2",h3:"h3",header:"header",li:"li",p:"p",pre:"pre",ul:"ul",...(0,o.R)(),...e.components};return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(n.header,{children:(0,r.jsx)(n.h1,{id:"decorator-handlers",children:"Decorator Handlers"})}),"\n",(0,r.jsxs)(n.p,{children:["If you don't want to use the ",(0,r.jsx)(n.code,{children:"add_handler"})," method, you can use decorators to register handlers to the app."]}),"\n",(0,r.jsx)(n.h2,{id:"decorators",children:"Decorators"}),"\n",(0,r.jsxs)(n.p,{children:["There are one to one matching decorators for each of the existing ",(0,r.jsx)(n.a,{href:"./handlers",children:(0,r.jsx)(n.code,{children:"handlers"})})," methods."]}),"\n",(0,r.jsxs)(n.p,{children:["Let's say that you have defined your app as ",(0,r.jsx)(n.code,{children:"app"}),", then you can use the following decorators to register handlers (change the ",(0,r.jsx)(n.code,{children:"app"})," variable to whatever you have defined your app as):"]}),"\n",(0,r.jsxs)(n.ul,{children:["\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_message"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_callback_query"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_command"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_channel_created"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_channel_updated"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_channel_deleted"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_group_created"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_group_updated"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_group_deleted"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_community_updated"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_member_joined"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_member_left"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_user_banned"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_unknown_command"})}),"\n",(0,r.jsx)(n.li,{children:(0,r.jsx)(n.code,{children:"@app.on_inline_query"})}),"\n"]}),"\n",(0,r.jsx)(n.p,{children:"The decorators are functions that take a function as an argument and return a function. The function that is returned is the handler that is registered to the app as a callback."}),"\n",(0,r.jsxs)(n.p,{children:["All of the decorators take the same arguments as the corresponding handler method. For example, the ",(0,r.jsx)(n.code,{children:"@app.on_message"})," decorator takes the same arguments as the ",(0,r.jsx)(n.code,{children:"app.add_handler(MessageHandler(...))"})," method, with the exception of the ",(0,r.jsx)(n.code,{children:"callback"})," argument, which is the function that is decorated."]}),"\n",(0,r.jsx)(n.h3,{id:"example",children:"Example"}),"\n",(0,r.jsx)(n.pre,{children:(0,r.jsx)(n.code,{className:"language-python",children:'from swibots import Client, MessageEvent, BotContext\n\napp = Client("token", "your bot description")\n\n@app.on_message()\nasync def message_handler(ctx: BotContext[MessageEvent]):\n   await ctx.event.message.reply_text(f"Thank you! I received your message: {ctx.event.message.message}")\n\napp.run()\n'})})]})}function h(e={}){const{wrapper:n}={...(0,o.R)(),...e.components};return n?(0,r.jsx)(n,{...e,children:(0,r.jsx)(l,{...e})}):l(e)}},8453:(e,n,t)=>{t.d(n,{R:()=>s,x:()=>d});var r=t(6540);const o={},a=r.createContext(o);function s(e){const n=r.useContext(a);return r.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function d(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(o):e.components||o:s(e.components),r.createElement(a.Provider,{value:n},e.children)}}}]);