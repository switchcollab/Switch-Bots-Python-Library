"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[2933],{351:(e,n,i)=>{i.r(n),i.d(n,{assets:()=>o,contentTitle:()=>a,default:()=>d,frontMatter:()=>c,metadata:()=>t,toc:()=>r});const t=JSON.parse('{"id":"mini-apps/components/FilePicker","title":"FilePicker","description":"FilePicker","source":"@site/docs/mini-apps/components/FilePicker.md","sourceDirName":"mini-apps/components","slug":"/mini-apps/components/FilePicker","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/FilePicker","draft":false,"unlisted":false,"tags":[],"version":"current","frontMatter":{},"sidebar":"tutorialSidebar","previous":{"title":"Embed","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/Embed"},"next":{"title":"Grid","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/Grid"}}');var s=i(4848),l=i(8453);const c={},a=void 0,o={},r=[{value:"FilePicker",id:"filepicker",level:3},{value:"Properties",id:"properties",level:4},{value:"Usage Example",id:"usage-example",level:4}];function p(e){const n={admonition:"admonition",code:"code",h3:"h3",h4:"h4",li:"li",p:"p",pre:"pre",ul:"ul",...(0,l.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(n.h3,{id:"filepicker",children:"FilePicker"}),"\n",(0,s.jsxs)(n.p,{children:["The ",(0,s.jsx)(n.code,{children:"FilePicker"})," class represents a component for selecting files in a user interface."]}),"\n",(0,s.jsx)(n.h4,{id:"properties",children:"Properties"}),"\n",(0,s.jsxs)(n.ul,{children:["\n",(0,s.jsxs)(n.li,{children:[(0,s.jsx)(n.code,{children:"callback_data"})," (Required): Data associated with a callback."]}),"\n",(0,s.jsxs)(n.li,{children:[(0,s.jsx)(n.code,{children:"files_count"})," (Optional): The maximum number of files that can be selected (default is 1)."]}),"\n",(0,s.jsxs)(n.li,{children:[(0,s.jsx)(n.code,{children:"mime_type"}),' (Optional): A list of allowed file types based on MIME types. By default, it allows "png", "jpg", "jpeg", and "webp" files.']}),"\n"]}),"\n",(0,s.jsx)(n.h4,{id:"usage-example",children:"Usage Example"}),"\n",(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{className:"language-python",children:'# Create a FilePicker instance:\nfile_picker = FilePicker(\n    callback_data="FilePickerCallback",\n    files_count=1,\n    mime_type=["png", "jpg", "jpeg", "webp"]\n)\n'})}),"\n",(0,s.jsxs)(n.admonition,{type:"note",children:[(0,s.jsx)(n.p,{children:"The response can be obtained as shown below:"}),(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{className:"language-python",children:'@app.on_callback_query(regexp(...))\nasync def onCallback(ctx: BotContext[CallbackQueryEvent]):\n    details = ctx.event.details\n    print("User Upload", details.file_name, details.file_url)\n'})})]})]})}function d(e={}){const{wrapper:n}={...(0,l.R)(),...e.components};return n?(0,s.jsx)(n,{...e,children:(0,s.jsx)(p,{...e})}):p(e)}},8453:(e,n,i)=>{i.d(n,{R:()=>c,x:()=>a});var t=i(6540);const s={},l=t.createContext(s);function c(e){const n=t.useContext(l);return t.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function a(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(s):e.components||s:c(e.components),t.createElement(l.Provider,{value:n},e.children)}}}]);