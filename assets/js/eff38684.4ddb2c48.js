"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[9717],{7020:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>l,contentTitle:()=>i,default:()=>u,frontMatter:()=>o,metadata:()=>s,toc:()=>c});var a=t(4848),r=t(8453);const o={},i="InlineMarkup",s={id:"api_reference/types/inline_markup",title:"InlineMarkup",description:"Class swibots.api.chat.models.InlineMarkup",source:"@site/docs/api_reference/types/inline_markup.md",sourceDirName:"api_reference/types",slug:"/api_reference/types/inline_markup",permalink:"/Switch-Bots-Python-Library/docs/api_reference/types/inline_markup",draft:!1,unlisted:!1,tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"InlineKeyboardButton",permalink:"/Switch-Bots-Python-Library/docs/api_reference/types/inline_keyboard_button"},next:{title:"Media",permalink:"/Switch-Bots-Python-Library/docs/api_reference/types/media"}},l={},c=[{value:"Properties",id:"properties",level:2},{value:"Usage",id:"usage",level:2}];function d(e){const n={a:"a",code:"code",h1:"h1",h2:"h2",header:"header",li:"li",p:"p",pre:"pre",ul:"ul",...(0,r.R)(),...e.components};return(0,a.jsxs)(a.Fragment,{children:[(0,a.jsx)(n.header,{children:(0,a.jsx)(n.h1,{id:"inlinemarkup",children:"InlineMarkup"})}),"\n",(0,a.jsx)(n.p,{children:(0,a.jsx)(n.code,{children:"Class swibots.api.chat.models.InlineMarkup"})}),"\n",(0,a.jsxs)(n.p,{children:["The ",(0,a.jsx)(n.code,{children:"InlineMarkup"})," class represents a markup that can be added to a message (Only bots can add markup to the messages)."]}),"\n",(0,a.jsx)(n.h2,{id:"properties",children:"Properties"}),"\n",(0,a.jsxs)(n.ul,{children:["\n",(0,a.jsxs)(n.li,{children:[(0,a.jsx)(n.code,{children:"inline_keyboard"})," (List[List[",(0,a.jsx)(n.a,{href:"./inline_keyboard_button",children:"InlineKeyboardButton"}),"]]): The markup's buttons."]}),"\n"]}),"\n",(0,a.jsx)(n.h2,{id:"usage",children:"Usage"}),"\n",(0,a.jsx)(n.pre,{children:(0,a.jsx)(n.code,{className:"language-python",children:'from swibots import InlineKeyboardButton, InlineMarkup\n\nbutton1 = InlineKeyboardButton(\n    text="Button Text",\n    url="https://example.com",\n    callback_data="callback_data"\n)\n\nbutton2 = InlineKeyboardButton(\n    text="Button Text",\n    url="https://example.com",\n    callback_data="callback_data"\n)\n\nbutton3 = InlineKeyboardButton(\n    text="Button Text",\n    url="https://example.com",\n    callback_data="callback_data"\n)\n\n## create a row of buttons\nrow1 = [button1, button2, button3]\n\n# add the row to the keyboard\n\nkeyboard = InlineMarkup(inline_keyboard=[row1])\n\n# add the keyboard to the message\n\nmessage = Message(text="Hello World", inline_markup=keyboard)\n\n'})})]})}function u(e={}){const{wrapper:n}={...(0,r.R)(),...e.components};return n?(0,a.jsx)(n,{...e,children:(0,a.jsx)(d,{...e})}):d(e)}},8453:(e,n,t)=>{t.d(n,{R:()=>i,x:()=>s});var a=t(6540);const r={},o=a.createContext(r);function i(e){const n=a.useContext(o);return a.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function s(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:i(e.components),a.createElement(o.Provider,{value:n},e.children)}}}]);