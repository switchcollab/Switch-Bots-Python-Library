"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[9661],{8940:(e,n,a)=>{a.r(n),a.d(n,{assets:()=>o,contentTitle:()=>i,default:()=>d,frontMatter:()=>c,metadata:()=>s,toc:()=>l});var r=a(4848),t=a(8453);const c={},i="SearchBar",s={id:"mini-apps/components/SearchBar",title:"SearchBar",description:"The SearchBar class represents a search bar in a user interface.",source:"@site/docs/mini-apps/components/SearchBar.md",sourceDirName:"mini-apps/components",slug:"/mini-apps/components/SearchBar",permalink:"/Switch-Bots-Python-Library/docs/mini-apps/components/SearchBar",draft:!1,unlisted:!1,tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"ListView",permalink:"/Switch-Bots-Python-Library/docs/mini-apps/components/ListView"},next:{title:"SearchHolder",permalink:"/Switch-Bots-Python-Library/docs/mini-apps/components/SearchHolder"}},o={},l=[{value:"Properties",id:"properties",level:4},{value:"Usage Example",id:"usage-example",level:4}];function h(e){const n={admonition:"admonition",code:"code",h1:"h1",h4:"h4",header:"header",li:"li",p:"p",pre:"pre",ul:"ul",...(0,t.R)(),...e.components};return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(n.header,{children:(0,r.jsx)(n.h1,{id:"searchbar",children:"SearchBar"})}),"\n",(0,r.jsxs)(n.p,{children:["The ",(0,r.jsx)(n.code,{children:"SearchBar"})," class represents a search bar in a user interface."]}),"\n",(0,r.jsx)(n.h4,{id:"properties",children:"Properties"}),"\n",(0,r.jsxs)(n.ul,{children:["\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"placeholder"})," (Optional): The placeholder text for the search bar."]}),"\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"label"})," (Optional): The label for the search bar."]}),"\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"value"})," (Optional): The current value of the search bar."]}),"\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"right_icon"})," (Optional): The icon on the right side of the search bar."]}),"\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"left_icon"})," (Optional): The icon on the left side of the search bar."]}),"\n",(0,r.jsxs)(n.li,{children:[(0,r.jsx)(n.code,{children:"callback_data"})," (Optional): Data associated with a callback."]}),"\n"]}),"\n",(0,r.jsx)(n.h4,{id:"usage-example",children:"Usage Example"}),"\n",(0,r.jsx)(n.pre,{children:(0,r.jsx)(n.code,{className:"language-python",children:'# Create a SearchBar instance:\nsearch_bar = SearchBar(\n    placeholder="Search",\n    label="Search Label",\n    value="Initial Value",\n    right_icon="https://img.icons8.com/?size=50&id=12773&format=png",\n    left_icon="https://img.icons8.com/?size=50&id=47516&format=png",\n    callback_data="Callback Data"\n)\n'})}),"\n",(0,r.jsxs)(n.admonition,{type:"note",children:[(0,r.jsx)(n.p,{children:"The search query can be obtained as shown below:"}),(0,r.jsx)(n.pre,{children:(0,r.jsx)(n.code,{className:"language-python",children:'@app.on_callback_query(regexp(...))\nasync def onCallback(ctx: BotContext[CallbackQueryEvent]):\n    input_ = ctx.event.details.search_query\n    print("User searched for", input_)\n'})})]})]})}function d(e={}){const{wrapper:n}={...(0,t.R)(),...e.components};return n?(0,r.jsx)(n,{...e,children:(0,r.jsx)(h,{...e})}):h(e)}},8453:(e,n,a)=>{a.d(n,{R:()=>i,x:()=>s});var r=a(6540);const t={},c=r.createContext(t);function i(e){const n=r.useContext(c);return r.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function s(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(t):e.components||t:i(e.components),r.createElement(c.Provider,{value:n},e.children)}}}]);