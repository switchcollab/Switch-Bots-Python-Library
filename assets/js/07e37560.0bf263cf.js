"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[8078],{9187:(e,t,s)=>{s.r(t),s.d(t,{assets:()=>a,contentTitle:()=>o,default:()=>m,frontMatter:()=>r,metadata:()=>c,toc:()=>d});var i=s(4848),n=s(8453);const r={},o="get_community_media_files by status:",c={id:"api_reference/methods/get_community_media_files_by_status",title:"get_community_media_files by status:",description:"Get community media files by status.",source:"@site/docs/api_reference/methods/get_community_media_files_by_status.md",sourceDirName:"api_reference/methods",slug:"/api_reference/methods/get_community_media_files_by_status",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/get_community_media_files_by_status",draft:!1,unlisted:!1,tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"get_community_media_files:",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/get_community_media_files"},next:{title:"get_community_member",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/get_community_member"}},a={},d=[{value:"Parameters:",id:"parameters",level:3},{value:"Returns:",id:"returns",level:3},{value:"Raises:",id:"raises",level:3},{value:"Example:",id:"example",level:3}];function l(e){const t={a:"a",code:"code",h1:"h1",h3:"h3",header:"header",li:"li",p:"p",pre:"pre",ul:"ul",...(0,n.R)(),...e.components};return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(t.header,{children:(0,i.jsx)(t.h1,{id:"get_community_media_files-by-status",children:"get_community_media_files by status:"})}),"\n",(0,i.jsx)(t.p,{children:"Get community media files by status."}),"\n",(0,i.jsx)(t.h3,{id:"parameters",children:"Parameters:"}),"\n",(0,i.jsxs)(t.ul,{children:["\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"community_id"})," (",(0,i.jsx)(t.code,{children:"str"}),"): The ID of the community."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"status"})," (",(0,i.jsx)(t.code,{children:"int"})," | ",(0,i.jsx)(t.code,{children:"List[int]"}),"): status to look for."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"channel_id"})," (",(0,i.jsx)(t.code,{children:"str"}),", optional): Channel id"]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"group_id"})," (",(0,i.jsx)(t.code,{children:"str"}),", optional): group id"]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"user_id"})," (",(0,i.jsx)(t.code,{children:"str"}),", optional): user id"]}),"\n"]}),"\n",(0,i.jsx)(t.h3,{id:"returns",children:"Returns:"}),"\n",(0,i.jsxs)(t.ul,{children:["\n",(0,i.jsxs)(t.li,{children:["List[",(0,i.jsx)(t.a,{href:"/Switch-Bots-Python-Library/docs/api_reference/types/message",children:"Message"}),"]: A list of Message objects representing media files."]}),"\n"]}),"\n",(0,i.jsx)(t.h3,{id:"raises",children:"Raises:"}),"\n",(0,i.jsxs)(t.ul,{children:["\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"switch.error.SwitchError"}),": If the messages could not be retrieved."]}),"\n"]}),"\n",(0,i.jsx)(t.h3,{id:"example",children:"Example:"}),"\n",(0,i.jsx)(t.pre,{children:(0,i.jsx)(t.code,{className:"language-python",children:'# look for images\n\nmedia_files = await client.get_community_media_files_by_status(community_id="communityID", status=1)\nprint(media_files)\n\n# or to get the status, use enum\nfrom swibots.types import MediaType\n# status=MediaType.DOCUMENT.value\n'})})]})}function m(e={}){const{wrapper:t}={...(0,n.R)(),...e.components};return t?(0,i.jsx)(t,{...e,children:(0,i.jsx)(l,{...e})}):l(e)}},8453:(e,t,s)=>{s.d(t,{R:()=>o,x:()=>c});var i=s(6540);const n={},r=i.createContext(n);function o(e){const t=i.useContext(r);return i.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function c(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(n):e.components||n:o(e.components),i.createElement(r.Provider,{value:t},e.children)}}}]);