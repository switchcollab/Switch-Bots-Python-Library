"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[6337],{8839:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>a,contentTitle:()=>l,default:()=>h,frontMatter:()=>r,metadata:()=>o,toc:()=>c});const o=JSON.parse('{"id":"mini-apps/BottomBar","title":"BottomBar","description":"BottomBarTile","source":"@site/docs/mini-apps/BottomBar.md","sourceDirName":"mini-apps","slug":"/mini-apps/BottomBar","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/BottomBar","draft":false,"unlisted":false,"tags":[],"version":"current","sidebarPosition":3,"frontMatter":{"sidebar_position":3},"sidebar":"tutorialSidebar","previous":{"title":"AppPage","permalink":"/Switch-Bots-Python-Library/docs/mini-apps/AppPage"},"next":{"title":"Components","permalink":"/Switch-Bots-Python-Library/docs/category/components"}}');var i=n(4848),s=n(8453);const r={sidebar_position:3},l=void 0,a={},c=[{value:"BottomBarTile",id:"bottombartile",level:2},{value:"Properties",id:"properties",level:3},{value:"Methods",id:"methods",level:3},{value:"BottomBarType",id:"bottombartype",level:2},{value:"Enum Values",id:"enum-values",level:3},{value:"BottomBar",id:"bottombar",level:2},{value:"Properties",id:"properties-1",level:3},{value:"Methods",id:"methods-1",level:3},{value:"Usage Example:",id:"usage-example",level:3}];function d(e){const t={code:"code",h2:"h2",h3:"h3",li:"li",p:"p",pre:"pre",strong:"strong",ul:"ul",...(0,s.R)(),...e.components};return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(t.h2,{id:"bottombartile",children:"BottomBarTile"}),"\n",(0,i.jsx)(t.p,{children:"Represents a tile in the bottom bar of a user interface."}),"\n",(0,i.jsx)(t.h3,{id:"properties",children:"Properties"}),"\n",(0,i.jsxs)(t.ul,{children:["\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"name"})," (Required): The name of the tile."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"icon"})," (Optional): The icon URL of the tile."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"selected_icon"})," (Optional): The icon URL of the selected tile."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"dark_icon"})," (Optional): The icon URL of the tile in dark mode."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"dark_selection_icon"})," (Optional): The icon URL of the selected tile in dark mode."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"selected"})," (Optional): A boolean indicating whether the tile is selected."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"callback_data"})," (Optional): The callback data associated with the tile."]}),"\n"]}),"\n",(0,i.jsx)(t.h3,{id:"methods",children:"Methods"}),"\n",(0,i.jsxs)(t.ul,{children:["\n",(0,i.jsx)(t.li,{children:(0,i.jsx)(t.strong,{children:"Constructor"})}),"\n"]}),"\n",(0,i.jsx)(t.pre,{children:(0,i.jsx)(t.code,{className:"language-python",children:'def __init__(\n    self,\n    name: str,\n    icon: str = "",\n    selection_icon: str = "",\n    dark_icon: str = "",\n    dark_selection_icon: str = "",\n    callback_data: str = "",\n    selected: bool = False,\n)\n'})}),"\n",(0,i.jsx)(t.h2,{id:"bottombartype",children:"BottomBarType"}),"\n",(0,i.jsx)(t.p,{children:"Represents the type of the bottom bar."}),"\n",(0,i.jsx)(t.h3,{id:"enum-values",children:"Enum Values"}),"\n",(0,i.jsxs)(t.ul,{children:["\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"DEFAULT"}),": Default bottom bar."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"TOPLINE"}),": Top line bottom bar."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"BOTTOMLINE"}),": Bottom line bottom bar."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"TOP_NOTCH"}),": Top notch bottom bar."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"BOTTOM_NOTCH"}),": Bottom notch bottom bar."]}),"\n"]}),"\n",(0,i.jsx)(t.p,{children:"Each enum value corresponds to a specific layout style for the bottom bar in the user interface."}),"\n",(0,i.jsx)(t.h2,{id:"bottombar",children:"BottomBar"}),"\n",(0,i.jsx)(t.p,{children:"Represents the bottom bar component in a user interface."}),"\n",(0,i.jsx)(t.h3,{id:"properties-1",children:"Properties"}),"\n",(0,i.jsxs)(t.ul,{children:["\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"options"})," (Required): List of ",(0,i.jsx)(t.code,{children:"BottomBarTile"})," instances representing the tiles in the bottom bar."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"type"})," (Optional): The type of the bottom bar, specified by ",(0,i.jsx)(t.code,{children:"BottomBarType"}),"."]}),"\n",(0,i.jsxs)(t.li,{children:[(0,i.jsx)(t.code,{children:"theme_color"})," (Optional): The theme color of the bottom bar."]}),"\n"]}),"\n",(0,i.jsx)(t.h3,{id:"methods-1",children:"Methods"}),"\n",(0,i.jsx)(t.pre,{children:(0,i.jsx)(t.code,{className:"language-python",children:'def __init__(\n    self,\n    options: List[BottomBarTile],\n    type: BottomBarType = BottomBarType.DEFAULT,\n    theme_color: str = ""\n)\n'})}),"\n",(0,i.jsx)(t.h3,{id:"usage-example",children:"Usage Example:"}),"\n",(0,i.jsx)(t.pre,{children:(0,i.jsx)(t.code,{className:"language-python",children:'# Create a BottomBarTile instance:\ntiles = [\n    BottomBarTile(\n        name="Home", icon="https://example.com/home_icon.png",\n        selected=True\n    ),\n    BottomBarTile(\n        name="Saved", icon="https://example.com/saved.png",\n    ),\n    BottomBarTile(\n        name="Settings", icon="https://example.com/settings.png",\n    ),\n]\n\n# Create a BottomBar instance:\nbottom_bar = BottomBar(\n    options=tiles,\n    type=BottomBarType.DEFAULT,\n    theme_color="#ffffff"\n)\n'})})]})}function h(e={}){const{wrapper:t}={...(0,s.R)(),...e.components};return t?(0,i.jsx)(t,{...e,children:(0,i.jsx)(d,{...e})}):d(e)}},8453:(e,t,n)=>{n.d(t,{R:()=>r,x:()=>l});var o=n(6540);const i={},s=o.createContext(i);function r(e){const t=o.useContext(s);return o.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function l(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:r(e.components),o.createElement(s.Provider,{value:t},e.children)}}}]);