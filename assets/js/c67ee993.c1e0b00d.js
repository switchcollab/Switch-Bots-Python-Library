"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[4702],{793:(e,n,s)=>{s.r(n),s.d(n,{assets:()=>c,contentTitle:()=>o,default:()=>h,frontMatter:()=>d,metadata:()=>r,toc:()=>a});const r=JSON.parse('{"id":"api_reference/methods/send_message","title":"send_message","description":"Send a text message to a user, channel or group.","source":"@site/docs/api_reference/methods/send_message.md","sourceDirName":"api_reference/methods","slug":"/api_reference/methods/send_message","permalink":"/Switch-Bots-Python-Library/docs/api_reference/methods/send_message","draft":false,"unlisted":false,"tags":[],"version":"current","frontMatter":{},"sidebar":"tutorialSidebar","previous":{"title":"send_media","permalink":"/Switch-Bots-Python-Library/docs/api_reference/methods/send_media"},"next":{"title":"Send sticker","permalink":"/Switch-Bots-Python-Library/docs/api_reference/methods/send_sticker"}}');var i=s(4848),t=s(8453);const d={},o="send_message",c={},a=[{value:"Signature",id:"signature",level:2},{value:"Parameters",id:"parameters",level:2}];function l(e){const n={a:"a",code:"code",h1:"h1",h2:"h2",header:"header",li:"li",p:"p",pre:"pre",ul:"ul",...(0,t.R)(),...e.components};return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(n.header,{children:(0,i.jsx)(n.h1,{id:"send_message",children:"send_message"})}),"\n",(0,i.jsx)(n.p,{children:"Send a text message to a user, channel or group."}),"\n",(0,i.jsx)(n.h2,{id:"signature",children:"Signature"}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:"async def send_message(\n    message: str,\n    community_id: Optional[str] = None,\n    channel_id: Optional[str] = None,\n    group_id: Optional[str] = None,\n    user_id: Optional[int] = None,\n    user_session_id: Optional[str] = None,\n    embed_message: Optional[EmbeddedMedia] = None,\n    inline_markup: InlineMarkup = None,\n   ) -> Message:\n"})}),"\n",(0,i.jsx)(n.h2,{id:"parameters",children:"Parameters"}),"\n",(0,i.jsxs)(n.ul,{children:["\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"message"})," (",(0,i.jsx)(n.code,{children:"str"}),"): The message to send"]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"community_id"})," (",(0,i.jsx)(n.code,{children:"str"}),"): The community id to send message."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"group_id"})," (",(0,i.jsx)(n.code,{children:"str"}),"): The Group ID."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"channel_id"})," (",(0,i.jsx)(n.code,{children:"str"}),"): Channel ID."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"user_id"})," (",(0,i.jsx)(n.code,{children:"int"}),"): User ID to send message."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"user_session_id"})," (",(0,i.jsx)(n.code,{children:"str"}),"): Session ID, present if bot is added as channel in the community."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"embed_message"})," (",(0,i.jsx)(n.a,{href:"/Switch-Bots-Python-Library/docs/api_reference/types/embedded_media",children:"EmbeddedMedia"}),")."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"inline_markup"})," (",(0,i.jsx)(n.a,{href:"/Switch-Bots-Python-Library/docs/api_reference/types/inline_markup",children:"InlineMarkup"}),"): Inline Markup linked with message."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"document"})," (",(0,i.jsx)(n.code,{children:"str"}),"): Path to the local file to send as document."]}),"\n"]})]})}function h(e={}){const{wrapper:n}={...(0,t.R)(),...e.components};return n?(0,i.jsx)(n,{...e,children:(0,i.jsx)(l,{...e})}):l(e)}},8453:(e,n,s)=>{s.d(n,{R:()=>d,x:()=>o});var r=s(6540);const i={},t=r.createContext(i);function d(e){const n=r.useContext(t);return r.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function o(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:d(e.components),r.createElement(t.Provider,{value:n},e.children)}}}]);