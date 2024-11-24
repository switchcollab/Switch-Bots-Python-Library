"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[2882],{5939:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>r,contentTitle:()=>c,default:()=>h,frontMatter:()=>l,metadata:()=>o,toc:()=>a});const o=JSON.parse('{"id":"mini-apps/components/Button","title":"Button","description":"The Button class represents an action button in a user interface.","source":"@site/docs/mini-apps/components/Button.md","sourceDirName":"mini-apps/components","slug":"/mini-apps/components/Button","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/Button","draft":false,"unlisted":false,"tags":[],"version":"current","frontMatter":{},"sidebar":"tutorialSidebar","previous":{"title":"Badge","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/Badge"},"next":{"title":"ButtonGroup","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/components/ButtonGroup"}}');var i=t(4848),s=t(8453);const l={},c="Button",r={},a=[{value:"Properties",id:"properties",level:3},{value:"Methods",id:"methods",level:3},{value:"Usage Example",id:"usage-example",level:3},{value:"DownloadButton",id:"downloadbutton",level:2},{value:"Properties:",id:"properties-1",level:3},{value:"Constructor:",id:"constructor",level:3},{value:"Usage Example:",id:"usage-example-1",level:3},{value:"ShareButton",id:"sharebutton",level:2},{value:"Attributes:",id:"attributes",level:3},{value:"Usage Example:",id:"usage-example-2",level:3},{value:"ClipboardButton",id:"clipboardbutton",level:2},{value:"Attributes:",id:"attributes-1",level:3},{value:"Usage Example:",id:"usage-example-3",level:3}];function d(e){const n={code:"code",h1:"h1",h2:"h2",h3:"h3",header:"header",li:"li",p:"p",pre:"pre",strong:"strong",ul:"ul",...(0,s.R)(),...e.components};return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(n.header,{children:(0,i.jsx)(n.h1,{id:"button",children:"Button"})}),"\n",(0,i.jsxs)(n.p,{children:["The ",(0,i.jsx)(n.code,{children:"Button"})," class represents an action button in a user interface."]}),"\n",(0,i.jsx)(n.h3,{id:"properties",children:"Properties"}),"\n",(0,i.jsxs)(n.ul,{children:["\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"text"})," (Required): The text content of the button. It can be either a string or a ",(0,i.jsx)(n.code,{children:"Text"})," component."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"icon"})," (Optional): The icon associated with the button. It can be either a string (URL) or an ",(0,i.jsx)(n.code,{children:"Icon"})," component."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"callback_data"})," (Optional): Data associated with a callback."]}),"\n"]}),"\n",(0,i.jsx)(n.h3,{id:"methods",children:"Methods"}),"\n",(0,i.jsxs)(n.ul,{children:["\n",(0,i.jsx)(n.li,{children:(0,i.jsx)(n.strong,{children:"Constructor"})}),"\n"]}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:'def __init__(\n    self,\n    text: Union[str, Text],\n    icon: Union[str, Icon] = "",\n    color: str = "",\n    callback_data: Optional[str] = None,\n)\n'})}),"\n",(0,i.jsx)(n.h3,{id:"usage-example",children:"Usage Example"}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:'# Create a Button instance:\nbutton = Button(\n    text="Click Me",\n    icon="https://example.com/icon.png",\n    callback_data="Callback Data"\n)\n'})}),"\n",(0,i.jsx)(n.h2,{id:"downloadbutton",children:"DownloadButton"}),"\n",(0,i.jsxs)(n.p,{children:["Extends the ",(0,i.jsx)(n.code,{children:"Button"})," class to represent a button with download functionality."]}),"\n",(0,i.jsx)(n.h3,{id:"properties-1",children:"Properties:"}),"\n",(0,i.jsxs)(n.ul,{children:["\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"download_url"}),": The URL from which the file will be downloaded."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"file_name"}),": The name to be given to the downloaded file."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"text"}),' (Optional): The text to be displayed on the button. Default is "Download". It can be a string or a ',(0,i.jsx)(n.code,{children:"Text"})," object."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"icon"})," (Optional): An icon associated with the button. It can be a string (URL) or an ",(0,i.jsx)(n.code,{children:"Icon"})," component."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"callback_data"})," (Optional): Callback data associated with the button."]}),"\n"]}),"\n",(0,i.jsx)(n.h3,{id:"constructor",children:"Constructor:"}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:'def __init__(\n    self,\n    download_url: str,\n    file_name: str,\n    text: str | Text = "Download",\n    icon: str | Icon = "",\n    callback_data: str = None\n)\n'})}),"\n",(0,i.jsx)(n.h3,{id:"usage-example-1",children:"Usage Example:"}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:'download_button = DownloadButton(\n    download_url="https://example.com/file.zip",\n    file_name="example_file.zip",\n    text="Download File",\n    icon="https://example.com/download-icon.png",\n    callback_data="download_callback_data"\n)\n'})}),"\n",(0,i.jsx)(n.h2,{id:"sharebutton",children:"ShareButton"}),"\n",(0,i.jsxs)(n.p,{children:["Extends the ",(0,i.jsx)(n.code,{children:"Button"})," class to represent a button with share functionality."]}),"\n",(0,i.jsx)(n.h3,{id:"attributes",children:"Attributes:"}),"\n",(0,i.jsxs)(n.ul,{children:["\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"text"})," (",(0,i.jsx)(n.code,{children:"str"})," or ",(0,i.jsx)(n.code,{children:"Text"}),"): The text content of the button."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"share_text"})," (",(0,i.jsx)(n.code,{children:"str"}),"): The text to be shared when the button is clicked."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"icon"})," (",(0,i.jsx)(n.code,{children:"str"})," or ",(0,i.jsx)(n.code,{children:"Icon"}),", optional): The icon associated with the button."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"color"})," (",(0,i.jsx)(n.code,{children:"str"}),", optional): The color of the button."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"variant"})," (",(0,i.jsx)(n.code,{children:"ButtonVariant"}),", optional): The variant of the button."]}),"\n"]}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:'def __init__(\n    self,\n    text: str | Text,\n    icon: str | Icon = "",\n    share_text: str = "",\n    color: str = None,\n    variant: ButtonVariant = ButtonVariant.DEFAULT,\n)\n'})}),"\n",(0,i.jsx)(n.h3,{id:"usage-example-2",children:"Usage Example:"}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:'share_button = ShareButton(\n    text="Share",\n    share_text="Check out this awesome article!",\n)\n'})}),"\n",(0,i.jsx)(n.h2,{id:"clipboardbutton",children:"ClipboardButton"}),"\n",(0,i.jsx)(n.h3,{id:"attributes-1",children:"Attributes:"}),"\n",(0,i.jsxs)(n.ul,{children:["\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"text"})," (",(0,i.jsx)(n.code,{children:"str"})," or ",(0,i.jsx)(n.code,{children:"Text"}),"): The text content of the button."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"url"})," (",(0,i.jsx)(n.code,{children:"str"}),"): The URL or text to be copied to the clipboard when the button is clicked."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"icon"})," (",(0,i.jsx)(n.code,{children:"str"})," or ",(0,i.jsx)(n.code,{children:"Icon"}),", optional): The icon associated with the button."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"color"})," (",(0,i.jsx)(n.code,{children:"str"}),", optional): The color of the button."]}),"\n",(0,i.jsxs)(n.li,{children:[(0,i.jsx)(n.code,{children:"variant"})," (",(0,i.jsx)(n.code,{children:"ButtonVariant"}),", optional): The variant of the button."]}),"\n"]}),"\n",(0,i.jsx)(n.h3,{id:"usage-example-3",children:"Usage Example:"}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:'clipboard_button = ClipboardButton(\n    text="Copy Link",\n    url="https://example.com/page",\n)\n'})})]})}function h(e={}){const{wrapper:n}={...(0,s.R)(),...e.components};return n?(0,i.jsx)(n,{...e,children:(0,i.jsx)(d,{...e})}):d(e)}},8453:(e,n,t)=>{t.d(n,{R:()=>l,x:()=>c});var o=t(6540);const i={},s=o.createContext(i);function l(e){const n=o.useContext(s);return o.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function c(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:l(e.components),o.createElement(s.Provider,{value:n},e.children)}}}]);