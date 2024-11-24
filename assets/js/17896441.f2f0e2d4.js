"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[8401],{1243:(e,n,t)=>{t.d(n,{A:()=>v});t(6540);var s=t(8215),i=t(7559),a=t(4718),l=t(9169),o=t(8774),r=t(1312),c=t(6025),d=t(4848);function u(e){return(0,d.jsx)("svg",{viewBox:"0 0 24 24",...e,children:(0,d.jsx)("path",{d:"M10 19v-5h4v5c0 .55.45 1 1 1h3c.55 0 1-.45 1-1v-7h1.7c.46 0 .68-.57.33-.87L12.67 3.6c-.38-.34-.96-.34-1.34 0l-8.36 7.53c-.34.3-.13.87.33.87H5v7c0 .55.45 1 1 1h3c.55 0 1-.45 1-1z",fill:"currentColor"})})}const m={breadcrumbHomeIcon:"breadcrumbHomeIcon_YNFT"};function h(){const e=(0,c.Ay)("/");return(0,d.jsx)("li",{className:"breadcrumbs__item",children:(0,d.jsx)(o.A,{"aria-label":(0,r.T)({id:"theme.docs.breadcrumbs.home",message:"Home page",description:"The ARIA label for the home page in the breadcrumbs"}),className:"breadcrumbs__link",href:e,children:(0,d.jsx)(u,{className:m.breadcrumbHomeIcon})})})}const x={breadcrumbsContainer:"breadcrumbsContainer_Z_bl"};function f(e){let{children:n,href:t,isLast:s}=e;const i="breadcrumbs__link";return s?(0,d.jsx)("span",{className:i,itemProp:"name",children:n}):t?(0,d.jsx)(o.A,{className:i,href:t,itemProp:"item",children:(0,d.jsx)("span",{itemProp:"name",children:n})}):(0,d.jsx)("span",{className:i,children:n})}function p(e){let{children:n,active:t,index:i,addMicrodata:a}=e;return(0,d.jsxs)("li",{...a&&{itemScope:!0,itemProp:"itemListElement",itemType:"https://schema.org/ListItem"},className:(0,s.A)("breadcrumbs__item",{"breadcrumbs__item--active":t}),children:[n,(0,d.jsx)("meta",{itemProp:"position",content:String(i+1)})]})}function v(){const e=(0,a.OF)(),n=(0,l.Dt)();return e?(0,d.jsx)("nav",{className:(0,s.A)(i.G.docs.docBreadcrumbs,x.breadcrumbsContainer),"aria-label":(0,r.T)({id:"theme.docs.breadcrumbs.navAriaLabel",message:"Breadcrumbs",description:"The ARIA label for the breadcrumbs"}),children:(0,d.jsxs)("ul",{className:"breadcrumbs",itemScope:!0,itemType:"https://schema.org/BreadcrumbList",children:[n&&(0,d.jsx)(h,{}),e.map(((n,t)=>{const s=t===e.length-1,i="category"===n.type&&n.linkUnlisted?void 0:n.href;return(0,d.jsx)(p,{active:s,index:t,addMicrodata:!!i,children:(0,d.jsx)(f,{href:i,isLast:s,children:n.label})},t)}))]})}):null}},3762:(e,n,t)=>{t.r(n),t.d(n,{default:()=>un});var s=t(6540),i=t(9024),a=t(9532),l=t(4848);const o=s.createContext(null);function r(e){let{children:n,content:t}=e;const i=function(e){return(0,s.useMemo)((()=>({metadata:e.metadata,frontMatter:e.frontMatter,assets:e.assets,contentTitle:e.contentTitle,toc:e.toc})),[e])}(t);return(0,l.jsx)(o.Provider,{value:i,children:n})}function c(){const e=(0,s.useContext)(o);if(null===e)throw new a.dV("DocProvider");return e}function d(){const{metadata:e,frontMatter:n,assets:t}=c();return(0,l.jsx)(i.be,{title:e.title,description:e.description,keywords:n.keywords,image:t.image??n.image})}var u=t(8215),m=t(4581),h=t(6929);function x(){const{metadata:e}=c();return(0,l.jsx)(h.A,{previous:e.previous,next:e.next})}var f=t(1878),p=t(4267),v=t(7559),j=t(1312),g=t(8774);const b={tag:"tag_zVej",tagRegular:"tagRegular_sFm0",tagWithCount:"tagWithCount_h2kH"};function A(e){let{permalink:n,label:t,count:s,description:i}=e;return(0,l.jsxs)(g.A,{href:n,title:i,className:(0,u.A)(b.tag,s?b.tagWithCount:b.tagRegular),children:[t,s&&(0,l.jsx)("span",{children:s})]})}const N={tags:"tags_jXut",tag:"tag_QGVx"};function C(e){let{tags:n}=e;return(0,l.jsxs)(l.Fragment,{children:[(0,l.jsx)("b",{children:(0,l.jsx)(j.A,{id:"theme.tags.tagsListLabel",description:"The label alongside a tag list",children:"Tags:"})}),(0,l.jsx)("ul",{className:(0,u.A)(N.tags,"padding--none","margin-left--sm"),children:n.map((e=>(0,l.jsx)("li",{className:N.tag,children:(0,l.jsx)(A,{...e})},e.permalink)))})]})}const L={iconEdit:"iconEdit_Z9Sw"};function _(e){let{className:n,...t}=e;return(0,l.jsx)("svg",{fill:"currentColor",height:"20",width:"20",viewBox:"0 0 40 40",className:(0,u.A)(L.iconEdit,n),"aria-hidden":"true",...t,children:(0,l.jsx)("g",{children:(0,l.jsx)("path",{d:"m34.5 11.7l-3 3.1-6.3-6.3 3.1-3q0.5-0.5 1.2-0.5t1.1 0.5l3.9 3.9q0.5 0.4 0.5 1.1t-0.5 1.2z m-29.5 17.1l18.4-18.5 6.3 6.3-18.4 18.4h-6.3v-6.2z"})})})}function y(e){let{editUrl:n}=e;return(0,l.jsxs)(g.A,{to:n,className:v.G.common.editThisPage,children:[(0,l.jsx)(_,{}),(0,l.jsx)(j.A,{id:"theme.common.editThisPage",description:"The link label to edit the current page",children:"Edit this page"})]})}var T=t(4586);function k(e){void 0===e&&(e={});const{i18n:{currentLocale:n}}=(0,T.A)(),t=function(){const{i18n:{currentLocale:e,localeConfigs:n}}=(0,T.A)();return n[e].calendar}();return new Intl.DateTimeFormat(n,{calendar:t,...e})}function w(e){let{lastUpdatedAt:n}=e;const t=new Date(n),s=k({day:"numeric",month:"short",year:"numeric",timeZone:"UTC"}).format(t);return(0,l.jsx)(j.A,{id:"theme.lastUpdated.atDate",description:"The words used to describe on which date a page has been last updated",values:{date:(0,l.jsx)("b",{children:(0,l.jsx)("time",{dateTime:t.toISOString(),itemProp:"dateModified",children:s})})},children:" on {date}"})}function H(e){let{lastUpdatedBy:n}=e;return(0,l.jsx)(j.A,{id:"theme.lastUpdated.byUser",description:"The words used to describe by who the page has been last updated",values:{user:(0,l.jsx)("b",{children:n})},children:" by {user}"})}function M(e){let{lastUpdatedAt:n,lastUpdatedBy:t}=e;return(0,l.jsxs)("span",{className:v.G.common.lastUpdated,children:[(0,l.jsx)(j.A,{id:"theme.lastUpdated.lastUpdatedAtBy",description:"The sentence used to display when a page has been last updated, and by who",values:{atDate:n?(0,l.jsx)(w,{lastUpdatedAt:n}):"",byUser:t?(0,l.jsx)(H,{lastUpdatedBy:t}):""},children:"Last updated{atDate}{byUser}"}),!1]})}const B={lastUpdated:"lastUpdated_JAkA"};function U(e){let{className:n,editUrl:t,lastUpdatedAt:s,lastUpdatedBy:i}=e;return(0,l.jsxs)("div",{className:(0,u.A)("row",n),children:[(0,l.jsx)("div",{className:"col",children:t&&(0,l.jsx)(y,{editUrl:t})}),(0,l.jsx)("div",{className:(0,u.A)("col",B.lastUpdated),children:(s||i)&&(0,l.jsx)(M,{lastUpdatedAt:s,lastUpdatedBy:i})})]})}function E(){const{metadata:e}=c(),{editUrl:n,lastUpdatedAt:t,lastUpdatedBy:s,tags:i}=e,a=i.length>0,o=!!(n||t||s);return a||o?(0,l.jsxs)("footer",{className:(0,u.A)(v.G.docs.docFooter,"docusaurus-mt-lg"),children:[a&&(0,l.jsx)("div",{className:(0,u.A)("row margin-top--sm",v.G.docs.docFooterTagsRow),children:(0,l.jsx)("div",{className:"col",children:(0,l.jsx)(C,{tags:i})})}),o&&(0,l.jsx)(U,{className:(0,u.A)("margin-top--sm",v.G.docs.docFooterEditMetaRow),editUrl:n,lastUpdatedAt:t,lastUpdatedBy:s})]}):null}var I=t(1422),V=t(6342);function z(e){const n=e.map((e=>({...e,parentIndex:-1,children:[]}))),t=Array(7).fill(-1);n.forEach(((e,n)=>{const s=t.slice(2,e.level);e.parentIndex=Math.max(...s),t[e.level]=n}));const s=[];return n.forEach((e=>{const{parentIndex:t,...i}=e;t>=0?n[t].children.push(i):s.push(i)})),s}function R(e){let{toc:n,minHeadingLevel:t,maxHeadingLevel:s}=e;return n.flatMap((e=>{const n=R({toc:e.children,minHeadingLevel:t,maxHeadingLevel:s});return function(e){return e.level>=t&&e.level<=s}(e)?[{...e,children:n}]:n}))}function S(e){const n=e.getBoundingClientRect();return n.top===n.bottom?S(e.parentNode):n}function D(e,n){let{anchorTopOffset:t}=n;const s=e.find((e=>S(e).top>=t));if(s){return function(e){return e.top>0&&e.bottom<window.innerHeight/2}(S(s))?s:e[e.indexOf(s)-1]??null}return e[e.length-1]??null}function G(){const e=(0,s.useRef)(0),{navbar:{hideOnScroll:n}}=(0,V.p)();return(0,s.useEffect)((()=>{e.current=n?0:document.querySelector(".navbar").clientHeight}),[n]),e}function O(e){const n=(0,s.useRef)(void 0),t=G();(0,s.useEffect)((()=>{if(!e)return()=>{};const{linkClassName:s,linkActiveClassName:i,minHeadingLevel:a,maxHeadingLevel:l}=e;function o(){const e=function(e){return Array.from(document.getElementsByClassName(e))}(s),o=function(e){let{minHeadingLevel:n,maxHeadingLevel:t}=e;const s=[];for(let i=n;i<=t;i+=1)s.push(`h${i}.anchor`);return Array.from(document.querySelectorAll(s.join()))}({minHeadingLevel:a,maxHeadingLevel:l}),r=D(o,{anchorTopOffset:t.current}),c=e.find((e=>r&&r.id===function(e){return decodeURIComponent(e.href.substring(e.href.indexOf("#")+1))}(e)));e.forEach((e=>{!function(e,t){t?(n.current&&n.current!==e&&n.current.classList.remove(i),e.classList.add(i),n.current=e):e.classList.remove(i)}(e,e===c)}))}return document.addEventListener("scroll",o),document.addEventListener("resize",o),o(),()=>{document.removeEventListener("scroll",o),document.removeEventListener("resize",o)}}),[e,t])}function P(e){let{toc:n,className:t,linkClassName:s,isChild:i}=e;return n.length?(0,l.jsx)("ul",{className:i?void 0:t,children:n.map((e=>(0,l.jsxs)("li",{children:[(0,l.jsx)(g.A,{to:`#${e.id}`,className:s??void 0,dangerouslySetInnerHTML:{__html:e.value}}),(0,l.jsx)(P,{isChild:!0,toc:e.children,className:t,linkClassName:s})]},e.id)))}):null}const F=s.memo(P);function q(e){let{toc:n,className:t="table-of-contents table-of-contents__left-border",linkClassName:i="table-of-contents__link",linkActiveClassName:a,minHeadingLevel:o,maxHeadingLevel:r,...c}=e;const d=(0,V.p)(),u=o??d.tableOfContents.minHeadingLevel,m=r??d.tableOfContents.maxHeadingLevel,h=function(e){let{toc:n,minHeadingLevel:t,maxHeadingLevel:i}=e;return(0,s.useMemo)((()=>R({toc:z(n),minHeadingLevel:t,maxHeadingLevel:i})),[n,t,i])}({toc:n,minHeadingLevel:u,maxHeadingLevel:m});return O((0,s.useMemo)((()=>{if(i&&a)return{linkClassName:i,linkActiveClassName:a,minHeadingLevel:u,maxHeadingLevel:m}}),[i,a,u,m])),(0,l.jsx)(F,{toc:h,className:t,linkClassName:i,...c})}const W={tocCollapsibleButton:"tocCollapsibleButton_TO0P",tocCollapsibleButtonExpanded:"tocCollapsibleButtonExpanded_MG3E"};function $(e){let{collapsed:n,...t}=e;return(0,l.jsx)("button",{type:"button",...t,className:(0,u.A)("clean-btn",W.tocCollapsibleButton,!n&&W.tocCollapsibleButtonExpanded,t.className),children:(0,l.jsx)(j.A,{id:"theme.TOCCollapsible.toggleButtonLabel",description:"The label used by the button on the collapsible TOC component",children:"On this page"})})}const Z={tocCollapsible:"tocCollapsible_ETCw",tocCollapsibleContent:"tocCollapsibleContent_vkbj",tocCollapsibleExpanded:"tocCollapsibleExpanded_sAul"};function J(e){let{toc:n,className:t,minHeadingLevel:s,maxHeadingLevel:i}=e;const{collapsed:a,toggleCollapsed:o}=(0,I.u)({initialState:!0});return(0,l.jsxs)("div",{className:(0,u.A)(Z.tocCollapsible,!a&&Z.tocCollapsibleExpanded,t),children:[(0,l.jsx)($,{collapsed:a,onClick:o}),(0,l.jsx)(I.N,{lazy:!0,className:Z.tocCollapsibleContent,collapsed:a,children:(0,l.jsx)(q,{toc:n,minHeadingLevel:s,maxHeadingLevel:i})})]})}const Y={tocMobile:"tocMobile_ITEo"};function Q(){const{toc:e,frontMatter:n}=c();return(0,l.jsx)(J,{toc:e,minHeadingLevel:n.toc_min_heading_level,maxHeadingLevel:n.toc_max_heading_level,className:(0,u.A)(v.G.docs.docTocMobile,Y.tocMobile)})}const X={tableOfContents:"tableOfContents_bqdL",docItemContainer:"docItemContainer_F8PC"},K="table-of-contents__link toc-highlight",ee="table-of-contents__link--active";function ne(e){let{className:n,...t}=e;return(0,l.jsx)("div",{className:(0,u.A)(X.tableOfContents,"thin-scrollbar",n),children:(0,l.jsx)(q,{...t,linkClassName:K,linkActiveClassName:ee})})}function te(){const{toc:e,frontMatter:n}=c();return(0,l.jsx)(ne,{toc:e,minHeadingLevel:n.toc_min_heading_level,maxHeadingLevel:n.toc_max_heading_level,className:v.G.docs.docTocDesktop})}var se=t(1107),ie=t(8453),ae=t(5260),le=t(1432);function oe(e){return(0,l.jsx)("code",{...e})}var re=t(5066),ce=t(3427),de=t(2303);const ue="details_lb9f",me="isBrowser_bmU9",he="collapsibleContent_i85q";function xe(e){return!!e&&("SUMMARY"===e.tagName||xe(e.parentElement))}function fe(e,n){return!!e&&(e===n||fe(e.parentElement,n))}function pe(e){let{summary:n,children:t,...i}=e;(0,ce.A)().collectAnchor(i.id);const a=(0,de.A)(),o=(0,s.useRef)(null),{collapsed:r,setCollapsed:c}=(0,I.u)({initialState:!i.open}),[d,u]=(0,s.useState)(i.open),m=s.isValidElement(n)?n:(0,l.jsx)("summary",{children:n??"Details"});return(0,l.jsxs)("details",{...i,ref:o,open:d,"data-collapsed":r,className:(0,re.A)(ue,a&&me,i.className),onMouseDown:e=>{xe(e.target)&&e.detail>1&&e.preventDefault()},onClick:e=>{e.stopPropagation();const n=e.target;xe(n)&&fe(n,o.current)&&(e.preventDefault(),r?(c(!1),u(!0)):c(!0))},children:[m,(0,l.jsx)(I.N,{lazy:!1,collapsed:r,disableSSRStyle:!0,onCollapseTransitionEnd:e=>{c(e),u(!e)},children:(0,l.jsx)("div",{className:he,children:t})})]})}const ve="details_b_Ee";function je(e){let{...n}=e;return(0,l.jsx)(pe,{...n,className:(0,u.A)("alert alert--info",ve,n.className)})}function ge(e){const n=s.Children.toArray(e.children),t=n.find((e=>s.isValidElement(e)&&"summary"===e.type)),i=(0,l.jsx)(l.Fragment,{children:n.filter((e=>e!==t))});return(0,l.jsx)(je,{...e,summary:t,children:i})}function be(e){return(0,l.jsx)(se.A,{...e})}const Ae="containsTaskList_mC6p";function Ne(e){if(void 0!==e)return(0,u.A)(e,e?.includes("contains-task-list")&&Ae)}const Ce="img_ev3q";function Le(e){const{mdxAdmonitionTitle:n,rest:t}=function(e){const n=s.Children.toArray(e),t=n.find((e=>s.isValidElement(e)&&"mdxAdmonitionTitle"===e.type)),i=n.filter((e=>e!==t)),a=t?.props.children;return{mdxAdmonitionTitle:a,rest:i.length>0?(0,l.jsx)(l.Fragment,{children:i}):null}}(e.children),i=e.title??n;return{...e,...i&&{title:i},children:t}}const _e="admonition_xJq3",ye="admonitionHeading_Gvgb",Te="admonitionIcon_Rf37",ke="admonitionContent_BuS1";function we(e){let{type:n,className:t,children:s}=e;return(0,l.jsx)("div",{className:(0,u.A)(v.G.common.admonition,v.G.common.admonitionType(n),_e,t),children:s})}function He(e){let{icon:n,title:t}=e;return(0,l.jsxs)("div",{className:ye,children:[(0,l.jsx)("span",{className:Te,children:n}),t]})}function Me(e){let{children:n}=e;return n?(0,l.jsx)("div",{className:ke,children:n}):null}function Be(e){const{type:n,icon:t,title:s,children:i,className:a}=e;return(0,l.jsxs)(we,{type:n,className:a,children:[s||t?(0,l.jsx)(He,{title:s,icon:t}):null,(0,l.jsx)(Me,{children:i})]})}function Ue(e){return(0,l.jsx)("svg",{viewBox:"0 0 14 16",...e,children:(0,l.jsx)("path",{fillRule:"evenodd",d:"M6.3 5.69a.942.942 0 0 1-.28-.7c0-.28.09-.52.28-.7.19-.18.42-.28.7-.28.28 0 .52.09.7.28.18.19.28.42.28.7 0 .28-.09.52-.28.7a1 1 0 0 1-.7.3c-.28 0-.52-.11-.7-.3zM8 7.99c-.02-.25-.11-.48-.31-.69-.2-.19-.42-.3-.69-.31H6c-.27.02-.48.13-.69.31-.2.2-.3.44-.31.69h1v3c.02.27.11.5.31.69.2.2.42.31.69.31h1c.27 0 .48-.11.69-.31.2-.19.3-.42.31-.69H8V7.98v.01zM7 2.3c-3.14 0-5.7 2.54-5.7 5.68 0 3.14 2.56 5.7 5.7 5.7s5.7-2.55 5.7-5.7c0-3.15-2.56-5.69-5.7-5.69v.01zM7 .98c3.86 0 7 3.14 7 7s-3.14 7-7 7-7-3.12-7-7 3.14-7 7-7z"})})}const Ee={icon:(0,l.jsx)(Ue,{}),title:(0,l.jsx)(j.A,{id:"theme.admonition.note",description:"The default label used for the Note admonition (:::note)",children:"note"})};function Ie(e){return(0,l.jsx)(Be,{...Ee,...e,className:(0,u.A)("alert alert--secondary",e.className),children:e.children})}function Ve(e){return(0,l.jsx)("svg",{viewBox:"0 0 12 16",...e,children:(0,l.jsx)("path",{fillRule:"evenodd",d:"M6.5 0C3.48 0 1 2.19 1 5c0 .92.55 2.25 1 3 1.34 2.25 1.78 2.78 2 4v1h5v-1c.22-1.22.66-1.75 2-4 .45-.75 1-2.08 1-3 0-2.81-2.48-5-5.5-5zm3.64 7.48c-.25.44-.47.8-.67 1.11-.86 1.41-1.25 2.06-1.45 3.23-.02.05-.02.11-.02.17H5c0-.06 0-.13-.02-.17-.2-1.17-.59-1.83-1.45-3.23-.2-.31-.42-.67-.67-1.11C2.44 6.78 2 5.65 2 5c0-2.2 2.02-4 4.5-4 1.22 0 2.36.42 3.22 1.19C10.55 2.94 11 3.94 11 5c0 .66-.44 1.78-.86 2.48zM4 14h5c-.23 1.14-1.3 2-2.5 2s-2.27-.86-2.5-2z"})})}const ze={icon:(0,l.jsx)(Ve,{}),title:(0,l.jsx)(j.A,{id:"theme.admonition.tip",description:"The default label used for the Tip admonition (:::tip)",children:"tip"})};function Re(e){return(0,l.jsx)(Be,{...ze,...e,className:(0,u.A)("alert alert--success",e.className),children:e.children})}function Se(e){return(0,l.jsx)("svg",{viewBox:"0 0 14 16",...e,children:(0,l.jsx)("path",{fillRule:"evenodd",d:"M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"})})}const De={icon:(0,l.jsx)(Se,{}),title:(0,l.jsx)(j.A,{id:"theme.admonition.info",description:"The default label used for the Info admonition (:::info)",children:"info"})};function Ge(e){return(0,l.jsx)(Be,{...De,...e,className:(0,u.A)("alert alert--info",e.className),children:e.children})}function Oe(e){return(0,l.jsx)("svg",{viewBox:"0 0 16 16",...e,children:(0,l.jsx)("path",{fillRule:"evenodd",d:"M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"})})}const Pe={icon:(0,l.jsx)(Oe,{}),title:(0,l.jsx)(j.A,{id:"theme.admonition.warning",description:"The default label used for the Warning admonition (:::warning)",children:"warning"})};function Fe(e){return(0,l.jsx)("svg",{viewBox:"0 0 12 16",...e,children:(0,l.jsx)("path",{fillRule:"evenodd",d:"M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z"})})}const qe={icon:(0,l.jsx)(Fe,{}),title:(0,l.jsx)(j.A,{id:"theme.admonition.danger",description:"The default label used for the Danger admonition (:::danger)",children:"danger"})};const We={icon:(0,l.jsx)(Oe,{}),title:(0,l.jsx)(j.A,{id:"theme.admonition.caution",description:"The default label used for the Caution admonition (:::caution)",children:"caution"})};const $e={...{note:Ie,tip:Re,info:Ge,warning:function(e){return(0,l.jsx)(Be,{...Pe,...e,className:(0,u.A)("alert alert--warning",e.className),children:e.children})},danger:function(e){return(0,l.jsx)(Be,{...qe,...e,className:(0,u.A)("alert alert--danger",e.className),children:e.children})}},...{secondary:e=>(0,l.jsx)(Ie,{title:"secondary",...e}),important:e=>(0,l.jsx)(Ge,{title:"important",...e}),success:e=>(0,l.jsx)(Re,{title:"success",...e}),caution:function(e){return(0,l.jsx)(Be,{...We,...e,className:(0,u.A)("alert alert--warning",e.className),children:e.children})}}};function Ze(e){const n=Le(e),t=(s=n.type,$e[s]||(console.warn(`No admonition component found for admonition type "${s}". Using Info as fallback.`),$e.info));var s;return(0,l.jsx)(t,{...n})}const Je={Head:ae.A,details:ge,Details:ge,code:function(e){return function(e){return void 0!==e.children&&s.Children.toArray(e.children).every((e=>"string"==typeof e&&!e.includes("\n")))}(e)?(0,l.jsx)(oe,{...e}):(0,l.jsx)(le.A,{...e})},a:function(e){return(0,l.jsx)(g.A,{...e})},pre:function(e){return(0,l.jsx)(l.Fragment,{children:e.children})},ul:function(e){return(0,l.jsx)("ul",{...e,className:Ne(e.className)})},li:function(e){return(0,ce.A)().collectAnchor(e.id),(0,l.jsx)("li",{...e})},img:function(e){return(0,l.jsx)("img",{decoding:"async",loading:"lazy",...e,className:(n=e.className,(0,u.A)(n,Ce))});var n},h1:e=>(0,l.jsx)(be,{as:"h1",...e}),h2:e=>(0,l.jsx)(be,{as:"h2",...e}),h3:e=>(0,l.jsx)(be,{as:"h3",...e}),h4:e=>(0,l.jsx)(be,{as:"h4",...e}),h5:e=>(0,l.jsx)(be,{as:"h5",...e}),h6:e=>(0,l.jsx)(be,{as:"h6",...e}),admonition:Ze,mermaid:()=>null};function Ye(e){let{children:n}=e;return(0,l.jsx)(ie.x,{components:Je,children:n})}function Qe(e){let{children:n}=e;const t=function(){const{metadata:e,frontMatter:n,contentTitle:t}=c();return n.hide_title||void 0!==t?null:e.title}();return(0,l.jsxs)("div",{className:(0,u.A)(v.G.docs.docMarkdown,"markdown"),children:[t&&(0,l.jsx)("header",{children:(0,l.jsx)(se.A,{as:"h1",children:t})}),(0,l.jsx)(Ye,{children:n})]})}var Xe=t(1243);function Ke(){return(0,l.jsx)(j.A,{id:"theme.contentVisibility.unlistedBanner.title",description:"The unlisted content banner title",children:"Unlisted page"})}function en(){return(0,l.jsx)(j.A,{id:"theme.contentVisibility.unlistedBanner.message",description:"The unlisted content banner message",children:"This page is unlisted. Search engines will not index it, and only users having a direct link can access it."})}function nn(){return(0,l.jsx)(ae.A,{children:(0,l.jsx)("meta",{name:"robots",content:"noindex, nofollow"})})}function tn(){return(0,l.jsx)(j.A,{id:"theme.contentVisibility.draftBanner.title",description:"The draft content banner title",children:"Draft page"})}function sn(){return(0,l.jsx)(j.A,{id:"theme.contentVisibility.draftBanner.message",description:"The draft content banner message",children:"This page is a draft. It will only be visible in dev and be excluded from the production build."})}function an(e){let{className:n}=e;return(0,l.jsx)(Ze,{type:"caution",title:(0,l.jsx)(tn,{}),className:(0,u.A)(n,v.G.common.draftBanner),children:(0,l.jsx)(sn,{})})}function ln(e){let{className:n}=e;return(0,l.jsx)(Ze,{type:"caution",title:(0,l.jsx)(Ke,{}),className:(0,u.A)(n,v.G.common.unlistedBanner),children:(0,l.jsx)(en,{})})}function on(e){return(0,l.jsxs)(l.Fragment,{children:[(0,l.jsx)(nn,{}),(0,l.jsx)(ln,{...e})]})}function rn(e){let{metadata:n}=e;const{unlisted:t,frontMatter:s}=n;return(0,l.jsxs)(l.Fragment,{children:[(t||s.unlisted)&&(0,l.jsx)(on,{}),s.draft&&(0,l.jsx)(an,{})]})}const cn={docItemContainer:"docItemContainer_Djhp",docItemCol:"docItemCol_VOVn"};function dn(e){let{children:n}=e;const t=function(){const{frontMatter:e,toc:n}=c(),t=(0,m.l)(),s=e.hide_table_of_contents,i=!s&&n.length>0;return{hidden:s,mobile:i?(0,l.jsx)(Q,{}):void 0,desktop:!i||"desktop"!==t&&"ssr"!==t?void 0:(0,l.jsx)(te,{})}}(),{metadata:s}=c();return(0,l.jsxs)("div",{className:"row",children:[(0,l.jsxs)("div",{className:(0,u.A)("col",!t.hidden&&cn.docItemCol),children:[(0,l.jsx)(rn,{metadata:s}),(0,l.jsx)(f.A,{}),(0,l.jsxs)("div",{className:cn.docItemContainer,children:[(0,l.jsxs)("article",{children:[(0,l.jsx)(Xe.A,{}),(0,l.jsx)(p.A,{}),t.mobile,(0,l.jsx)(Qe,{children:n}),(0,l.jsx)(E,{})]}),(0,l.jsx)(x,{})]})]}),t.desktop&&(0,l.jsx)("div",{className:"col col--3",children:t.desktop})]})}function un(e){const n=`docs-doc-id-${e.content.metadata.id}`,t=e.content;return(0,l.jsx)(r,{content:e.content,children:(0,l.jsxs)(i.e3,{className:n,children:[(0,l.jsx)(d,{}),(0,l.jsx)(dn,{children:(0,l.jsx)(t,{})})]})})}},6929:(e,n,t)=>{t.d(n,{A:()=>r});t(6540);var s=t(1312),i=t(8215),a=t(8774),l=t(4848);function o(e){const{permalink:n,title:t,subLabel:s,isNext:o}=e;return(0,l.jsxs)(a.A,{className:(0,i.A)("pagination-nav__link",o?"pagination-nav__link--next":"pagination-nav__link--prev"),to:n,children:[s&&(0,l.jsx)("div",{className:"pagination-nav__sublabel",children:s}),(0,l.jsx)("div",{className:"pagination-nav__label",children:t})]})}function r(e){const{previous:n,next:t}=e;return(0,l.jsxs)("nav",{className:"pagination-nav docusaurus-mt-lg","aria-label":(0,s.T)({id:"theme.docs.paginator.navAriaLabel",message:"Docs pages",description:"The ARIA label for the docs pagination"}),children:[n&&(0,l.jsx)(o,{...n,subLabel:(0,l.jsx)(s.A,{id:"theme.docs.paginator.previous",description:"The label used to navigate to the previous doc",children:"Previous"})}),t&&(0,l.jsx)(o,{...t,subLabel:(0,l.jsx)(s.A,{id:"theme.docs.paginator.next",description:"The label used to navigate to the next doc",children:"Next"}),isNext:!0})]})}},4267:(e,n,t)=>{t.d(n,{A:()=>r});t(6540);var s=t(8215),i=t(1312),a=t(7559),l=t(3025),o=t(4848);function r(e){let{className:n}=e;const t=(0,l.r)();return t.badge?(0,o.jsx)("span",{className:(0,s.A)(n,a.G.docs.docVersionBadge,"badge badge--secondary"),children:(0,o.jsx)(i.A,{id:"theme.docs.versionBadge.label",values:{versionLabel:t.label},children:"Version: {versionLabel}"})}):null}},1878:(e,n,t)=>{t.d(n,{A:()=>p});t(6540);var s=t(8215),i=t(4586),a=t(8774),l=t(1312),o=t(4070),r=t(7559),c=t(3886),d=t(3025),u=t(4848);const m={unreleased:function(e){let{siteTitle:n,versionMetadata:t}=e;return(0,u.jsx)(l.A,{id:"theme.docs.versions.unreleasedVersionLabel",description:"The label used to tell the user that he's browsing an unreleased doc version",values:{siteTitle:n,versionLabel:(0,u.jsx)("b",{children:t.label})},children:"This is unreleased documentation for {siteTitle} {versionLabel} version."})},unmaintained:function(e){let{siteTitle:n,versionMetadata:t}=e;return(0,u.jsx)(l.A,{id:"theme.docs.versions.unmaintainedVersionLabel",description:"The label used to tell the user that he's browsing an unmaintained doc version",values:{siteTitle:n,versionLabel:(0,u.jsx)("b",{children:t.label})},children:"This is documentation for {siteTitle} {versionLabel}, which is no longer actively maintained."})}};function h(e){const n=m[e.versionMetadata.banner];return(0,u.jsx)(n,{...e})}function x(e){let{versionLabel:n,to:t,onClick:s}=e;return(0,u.jsx)(l.A,{id:"theme.docs.versions.latestVersionSuggestionLabel",description:"The label used to tell the user to check the latest version",values:{versionLabel:n,latestVersionLink:(0,u.jsx)("b",{children:(0,u.jsx)(a.A,{to:t,onClick:s,children:(0,u.jsx)(l.A,{id:"theme.docs.versions.latestVersionLinkLabel",description:"The label used for the latest version suggestion link label",children:"latest version"})})})},children:"For up-to-date documentation, see the {latestVersionLink} ({versionLabel})."})}function f(e){let{className:n,versionMetadata:t}=e;const{siteConfig:{title:a}}=(0,i.A)(),{pluginId:l}=(0,o.vT)({failfast:!0}),{savePreferredVersionName:d}=(0,c.g1)(l),{latestDocSuggestion:m,latestVersionSuggestion:f}=(0,o.HW)(l),p=m??(v=f).docs.find((e=>e.id===v.mainDocId));var v;return(0,u.jsxs)("div",{className:(0,s.A)(n,r.G.docs.docVersionBanner,"alert alert--warning margin-bottom--md"),role:"alert",children:[(0,u.jsx)("div",{children:(0,u.jsx)(h,{siteTitle:a,versionMetadata:t})}),(0,u.jsx)("div",{className:"margin-top--md",children:(0,u.jsx)(x,{versionLabel:f.label,to:p.path,onClick:()=>d(f.name)})})]})}function p(e){let{className:n}=e;const t=(0,d.r)();return t.banner?(0,u.jsx)(f,{className:n,versionMetadata:t}):null}},8453:(e,n,t)=>{t.d(n,{R:()=>l,x:()=>o});var s=t(6540);const i={},a=s.createContext(i);function l(e){const n=s.useContext(a);return s.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function o(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:l(e.components),s.createElement(a.Provider,{value:n},e.children)}}}]);