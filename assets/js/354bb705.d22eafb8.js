"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[4937],{6233:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>l,contentTitle:()=>r,default:()=>h,frontMatter:()=>s,metadata:()=>c,toc:()=>o});var a=t(4848),i=t(8453);const s={sidebar_position:3},r="Advertising",c={id:"interactions/advertising",title:"Advertising",description:"Earn Revenue with Switch Mini-Apps",source:"@site/docs/interactions/advertising.md",sourceDirName:"interactions",slug:"/interactions/advertising",permalink:"/Switch-Bots-Python-Library/docs/interactions/advertising",draft:!1,unlisted:!1,tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"tutorialSidebar",previous:{title:"Keyboards",permalink:"/Switch-Bots-Python-Library/docs/interactions/keyboards"},next:{title:"Inline queries",permalink:"/Switch-Bots-Python-Library/docs/interactions/inline_queries"}},l={},o=[{value:"Earn Revenue with Switch Mini-Apps",id:"earn-revenue-with-switch-mini-apps",level:2},{value:"How to apply for Ads Program?",id:"how-to-apply-for-ads-program",level:2},{value:"Integrating Bot to display Ads.",id:"integrating-bot-to-display-ads",level:2},{value:"Types of Ad",id:"types-of-ad",level:3},{value:"Preparing Bot to handle ads.",id:"preparing-bot-to-handle-ads",level:3},{value:"AdButton",id:"adbutton",level:3},{value:"Callbacks",id:"callbacks",level:3},{value:"Handling watched event.",id:"handling-watched-event",level:3}];function d(e){const n={a:"a",code:"code",h1:"h1",h2:"h2",h3:"h3",header:"header",li:"li",ol:"ol",p:"p",pre:"pre",ul:"ul",...(0,i.R)(),...e.components};return(0,a.jsxs)(a.Fragment,{children:[(0,a.jsx)(n.header,{children:(0,a.jsx)(n.h1,{id:"advertising",children:"Advertising"})}),"\n",(0,a.jsx)(n.h2,{id:"earn-revenue-with-switch-mini-apps",children:"Earn Revenue with Switch Mini-Apps"}),"\n",(0,a.jsxs)(n.ul,{children:["\n",(0,a.jsx)(n.li,{children:"Via Advertising from Switch Mini-Apps, app developers get an opportunity to earn and make their income."}),"\n"]}),"\n",(0,a.jsx)(n.h2,{id:"how-to-apply-for-ads-program",children:"How to apply for Ads Program?"}),"\n",(0,a.jsxs)(n.ol,{children:["\n",(0,a.jsx)(n.li,{children:"Find and open Monetize bot on Switch from apps section."}),"\n",(0,a.jsx)(n.li,{children:"On first open, It will ask you to apply for approval."}),"\n",(0,a.jsx)(n.li,{children:"Fill the basic required details, wait for approval."}),"\n"]}),"\n",(0,a.jsxs)(n.p,{children:["We provide responses within 24 hours, If, for your application it take long, ping us at ",(0,a.jsx)(n.a,{href:"https://iswitch.click/support",children:"Support Chat"})]}),"\n",(0,a.jsx)(n.h2,{id:"integrating-bot-to-display-ads",children:"Integrating Bot to display Ads."}),"\n",(0,a.jsx)(n.h3,{id:"types-of-ad",children:"Types of Ad"}),"\n",(0,a.jsx)(n.p,{children:"Currently, We support 2 types of Ads."}),"\n",(0,a.jsxs)(n.ol,{children:["\n",(0,a.jsxs)(n.li,{children:[(0,a.jsx)(n.code,{children:"VIDEO_1"}),": display one ad."]}),"\n",(0,a.jsxs)(n.li,{children:[(0,a.jsx)(n.code,{children:"VIDEO_2"}),": display two ads, one after other."]}),"\n"]}),"\n",(0,a.jsx)(n.p,{children:"Bot Developer can choose this according to there wish and place of integration."}),"\n",(0,a.jsx)(n.h3,{id:"preparing-bot-to-handle-ads",children:"Preparing Bot to handle ads."}),"\n",(0,a.jsxs)(n.ul,{children:["\n",(0,a.jsx)(n.li,{children:"Ads can be displayed any callback request."}),"\n"]}),"\n",(0,a.jsx)(n.p,{children:"Let's go step by step."}),"\n",(0,a.jsx)(n.h3,{id:"adbutton",children:"AdButton"}),"\n",(0,a.jsxs)(n.ol,{children:["\n",(0,a.jsx)(n.li,{children:"AdButton provide a different animation, which differs other button from Ad Buttons."}),"\n"]}),"\n",(0,a.jsx)(n.p,{children:"We created a page, where"}),"\n",(0,a.jsx)(n.pre,{children:(0,a.jsx)(n.code,{className:"language-python",children:'from swibots import AdButton\n\n@client.on_callback_query(regexp("page"))\nasync def __e(ctx: BotContext[CallbackQueryEvent]):\n    # We added 2 ad buttons\n    # ad_1 for type 1\n    # ad_2 for type 2\n    # in Next step, we add callbacks to callback data.\n    page = AppPage(\n            components=[\n                Text("Click below button to open ad."),\n                AdButton("Watch Ad [1]", callback_data="ad_1"),\n                AdButton("Watch Ad [2]", callback_data="ad_2"),\n            ]\n        )\n    await ctx.event.answer(\n        callback=page\n    )\n'})}),"\n",(0,a.jsx)(n.h3,{id:"callbacks",children:"Callbacks"}),"\n",(0,a.jsx)(n.p,{children:"We created the callback handlers, which"}),"\n",(0,a.jsxs)(n.ul,{children:["\n",(0,a.jsxs)(n.li,{children:["We define a ",(0,a.jsx)(n.code,{children:"success_callback"}),", which is a callback data, which is triggered after user watch the ads successfully."]}),"\n"]}),"\n",(0,a.jsx)(n.pre,{children:(0,a.jsx)(n.code,{className:"language-python",children:'@client.on_callback_query(regexp("ad_1"))\nasync def e(ctx: BotContext[CallbackQueryEvent]):\n    print(ctx)\n    await ctx.event.show_ad(\n        ad_type="VIDEO_1",\n        id="9195dwda-jnfafWasl-fflsle2",\n        success_callback="Success"\n        \n    )\n\n@client.on_callback_query(regexp("ad_2"))\nasync def __e(ctx: BotContext[CallbackQueryEvent]):\n    print(ctx)\n    await ctx.event.show_ad(\n        ad_type="VIDEO_2",\n        id="e452-sjgmamsmf-fjnsndl-kk7af",\n        success_callback="Success"\n    )\n'})}),"\n",(0,a.jsx)(n.h3,{id:"handling-watched-event",children:"Handling watched event."}),"\n",(0,a.jsxs)(n.ul,{children:["\n",(0,a.jsx)(n.li,{children:"We defined the success_callback in previous step, we can perform any action when the user watched the ad completely."}),"\n"]}),"\n",(0,a.jsx)(n.pre,{children:(0,a.jsx)(n.code,{className:"language-python",children:'@client.on_callback_query(regexp("Success"))\nasync def __e(ctx: BotContext[CallbackQueryEvent]):\n    await ctx.event.answer("Showed", show_alert=True)\n'})}),"\n",(0,a.jsx)(n.p,{children:(0,a.jsx)(n.a,{href:"https://github.com/switchcollab/Switch-Bots-Python-Library/blob/main/samples/ads.py",children:"Check the Complete Code Sample"})})]})}function h(e={}){const{wrapper:n}={...(0,i.R)(),...e.components};return n?(0,a.jsx)(n,{...e,children:(0,a.jsx)(d,{...e})}):d(e)}},8453:(e,n,t)=>{t.d(n,{R:()=>r,x:()=>c});var a=t(6540);const i={},s=a.createContext(i);function r(e){const n=a.useContext(s);return a.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function c(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:r(e.components),a.createElement(s.Provider,{value:n},e.children)}}}]);