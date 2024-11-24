"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[8297],{9788:(e,n,o)=>{o.r(n),o.d(n,{assets:()=>c,contentTitle:()=>a,default:()=>d,frontMatter:()=>i,metadata:()=>t,toc:()=>l});const t=JSON.parse('{"id":"mini-apps/components/Dropdown","title":"Dropdown","description":"The Dropdown class represents a dropdown in a user interface.","source":"@site/docs/mini-apps/components/Dropdown.md","sourceDirName":"mini-apps/components","slug":"/mini-apps/components/Dropdown","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/Dropdown","draft":false,"unlisted":false,"tags":[],"version":"current","frontMatter":{},"sidebar":"tutorialSidebar","previous":{"title":"Carousel","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/Carousel"},"next":{"title":"Embed","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/Embed"}}');var r=o(4848),s=o(8453);const i={},a="Dropdown",c={},l=[{value:"Properties",id:"properties",level:2},{value:"Example",id:"example",level:2}];function p(e){const n={code:"code",h1:"h1",h2:"h2",header:"header",li:"li",p:"p",pre:"pre",ul:"ul",...(0,s.R)(),...e.components};return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(n.header,{children:(0,r.jsx)(n.h1,{id:"dropdown",children:"Dropdown"})}),"\n",(0,r.jsxs)(n.p,{children:["The ",(0,r.jsx)(n.code,{children:"Dropdown"})," class represents a dropdown in a user interface."]}),"\n",(0,r.jsx)(n.h2,{id:"properties",children:"Properties"}),"\n",(0,r.jsxs)(n.ul,{children:["\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"placeholder"})," (Optional, ",(0,r.jsx)(n.code,{children:"str"}),"): The placeholder text for the dropdown."]}),"\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"selected"})," (Optional, ",(0,r.jsx)(n.code,{children:"int"}),"): The index of the selected item in the dropdown."]}),"\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"options"})," (List[ListTile]): A list of items representing the dropdown options."]}),"\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"disabled"})," (Optional, ",(0,r.jsx)(n.code,{children:"bool"}),"): A flag indicating whether the dropdown is disabled."]}),"\n"]}),"\n",(0,r.jsx)(n.h2,{id:"example",children:"Example"}),"\n",(0,r.jsx)(n.pre,{children:(0,r.jsx)(n.code,{className:"language-python",children:'from swibots import CallbackQueryEvent, BotContext\nfrom swibots import AppPage, AppBar, Dropdown, ListItem\n\n# handle callback query\n@app.on_callback_query()\nasync def onCallback(ctx: BotContext[CallbackQueryEvent]):\n    # create a callback component\n    await ctx.event.answer(\n        callback=AppPage(\n            app_bar=AppBar(title="Hello from Swibots"),\n            components=[\n                Dropdown(\n                    placeholder="Choose Option",\n                    options=[\n                        ListItem("1. Orange", callback_data="option1"),\n                        ListItem("2. Yellow", callback_data="option2"),\n                        ListItem("3. Green", callback_data="option3"),\n                        ListItem("4. Green", callback_data="option4"),\n                    ],\n                )\n            ],\n        )\n    )\n'})})]})}function d(e={}){const{wrapper:n}={...(0,s.R)(),...e.components};return n?(0,r.jsx)(n,{...e,children:(0,r.jsx)(p,{...e})}):p(e)}},8453:(e,n,o)=>{o.d(n,{R:()=>i,x:()=>a});var t=o(6540);const r={},s=t.createContext(r);function i(e){const n=t.useContext(s);return t.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function a(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:i(e.components),t.createElement(s.Provider,{value:n},e.children)}}}]);