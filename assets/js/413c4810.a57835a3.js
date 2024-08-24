"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[195],{8746:(e,n,s)=>{s.r(n),s.d(n,{assets:()=>a,contentTitle:()=>l,default:()=>h,frontMatter:()=>r,metadata:()=>i,toc:()=>d});var t=s(4848),o=s(8453);const r={sidebar_position:1},l="Deploy on Ubuntu/Debian",i={id:"deploy/ubuntu",title:"Deploy on Ubuntu/Debian",description:"After you have created your bot, you should deply it on a server (you can also run it locally, but that would require you to have your pc always on).",source:"@site/docs/deploy/ubuntu.md",sourceDirName:"deploy",slug:"/deploy/ubuntu",permalink:"/Switch-Bots-Python-Library/docs/deploy/ubuntu",draft:!1,unlisted:!1,tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Deploy",permalink:"/Switch-Bots-Python-Library/docs/category/deploy"},next:{title:"Bots",permalink:"/Switch-Bots-Python-Library/docs/fundamentals/bots"}},a={},d=[{value:"Install Python 3.10 (if not available in the default repositories)",id:"install-python-310-if-not-available-in-the-default-repositories",level:2},{value:"Install dependencies",id:"install-dependencies",level:2},{value:"Run the bot",id:"run-the-bot",level:2},{value:"Run the bot on startup",id:"run-the-bot-on-startup",level:2},{value:"Using systemd",id:"using-systemd",level:3}];function c(e){const n={code:"code",em:"em",h1:"h1",h2:"h2",h3:"h3",header:"header",li:"li",ol:"ol",p:"p",pre:"pre",ul:"ul",...(0,o.R)(),...e.components};return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(n.header,{children:(0,t.jsx)(n.h1,{id:"deploy-on-ubuntudebian",children:"Deploy on Ubuntu/Debian"})}),"\n",(0,t.jsx)(n.p,{children:"After you have created your bot, you should deply it on a server (you can also run it locally, but that would require you to have your pc always on)."}),"\n",(0,t.jsx)(n.p,{children:"To deploy your bot on Ubuntu/Debian, please make sure you have installed the following dependencies:"}),"\n",(0,t.jsxs)(n.ul,{children:["\n",(0,t.jsxs)(n.li,{children:[(0,t.jsx)(n.code,{children:"python"})," 3.10 or higher (you can check your Python version by running ",(0,t.jsx)(n.code,{children:"python3 --version"}),")"]}),"\n",(0,t.jsxs)(n.li,{children:[(0,t.jsx)(n.code,{children:"pip"})," (you can check your ",(0,t.jsx)(n.code,{children:"pip"})," version by running ",(0,t.jsx)(n.code,{children:"pip3 --version"}),")"]}),"\n"]}),"\n",(0,t.jsx)(n.p,{children:(0,t.jsx)(n.em,{children:"Not required, but recommended:"})}),"\n",(0,t.jsxs)(n.ul,{children:["\n",(0,t.jsxs)(n.li,{children:[(0,t.jsx)(n.code,{children:"venv"})," (you can check your ",(0,t.jsx)(n.code,{children:"venv"})," version by running ",(0,t.jsx)(n.code,{children:"python3 -m venv --version"}),")"]}),"\n",(0,t.jsxs)(n.li,{children:[(0,t.jsx)(n.code,{children:"git"})," (you can check your ",(0,t.jsx)(n.code,{children:"git"})," version by running ",(0,t.jsx)(n.code,{children:"git --version"}),")"]}),"\n"]}),"\n",(0,t.jsx)(n.h2,{id:"install-python-310-if-not-available-in-the-default-repositories",children:"Install Python 3.10 (if not available in the default repositories)"}),"\n",(0,t.jsx)(n.p,{children:"Python 3.10 is not available in the default Ubuntu repositories. You can install it by following the steps below:"}),"\n",(0,t.jsxs)(n.ol,{children:["\n",(0,t.jsx)(n.li,{children:"Add the deadsnakes PPA:"}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"sudo add-apt-repository ppa:deadsnakes/ppa\n"})}),"\n",(0,t.jsxs)(n.ol,{start:"2",children:["\n",(0,t.jsx)(n.li,{children:"Update the package list:"}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"sudo apt update\n"})}),"\n",(0,t.jsxs)(n.ol,{start:"3",children:["\n",(0,t.jsx)(n.li,{children:"Install Python 3.10:"}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"sudo apt install python3.10\n"})}),"\n",(0,t.jsxs)(n.ol,{start:"4",children:["\n",(0,t.jsxs)(n.li,{children:["Install ",(0,t.jsx)(n.code,{children:"pip"})," for Python 3.10:"]}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"sudo apt install python3.10-distutils\ncurl https://bootstrap.pypa.io/get-pip.py | sudo python3.10\n"})}),"\n",(0,t.jsx)(n.h2,{id:"install-dependencies",children:"Install dependencies"}),"\n",(0,t.jsx)(n.p,{children:"To install the dependencies, run the following commands:"}),"\n",(0,t.jsx)(n.p,{children:(0,t.jsx)(n.em,{children:"If you have a requirements.txt file:"})}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"pip3 install -r requirements.txt\n"})}),"\n",(0,t.jsx)(n.p,{children:(0,t.jsx)(n.em,{children:"If you don't have a requirements.txt file:"})}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"pip3 install swibots\n"})}),"\n",(0,t.jsx)(n.p,{children:"Install other dependencies if you need them."}),"\n",(0,t.jsx)(n.h2,{id:"run-the-bot",children:"Run the bot"}),"\n",(0,t.jsx)(n.p,{children:"To run the bot, run the following command:"}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"python3 <your bot file>.py\n"})}),"\n",(0,t.jsx)(n.h2,{id:"run-the-bot-on-startup",children:"Run the bot on startup"}),"\n",(0,t.jsxs)(n.p,{children:["To run the bot on startup, you can use ",(0,t.jsx)(n.code,{children:"systemd"})," or ",(0,t.jsx)(n.code,{children:"supervisor"}),"."]}),"\n",(0,t.jsx)(n.h3,{id:"using-systemd",children:"Using systemd"}),"\n",(0,t.jsxs)(n.p,{children:["To run the bot on startup using ",(0,t.jsx)(n.code,{children:"systemd"}),", you can follow the steps below:"]}),"\n",(0,t.jsxs)(n.ol,{children:["\n",(0,t.jsx)(n.li,{children:"Create a service file for your bot. You can use the following template:"}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-ini",children:"[Unit]\nDescription=<your bot name>\nAfter=network.target\nStartLimitIntervalSec=0\n\n[Service]\nType=simple\nRestart=always\nRestartSec=1\nUser=<your user>\nExecStart=python3 /path/to/bot.py\n\n[Install]\nWantedBy=multi-user.target\n\n"})}),"\n",(0,t.jsxs)(n.ol,{start:"2",children:["\n",(0,t.jsxs)(n.li,{children:["\n",(0,t.jsxs)(n.p,{children:["Save the file as ",(0,t.jsx)(n.code,{children:"/etc/systemd/system/<your bot name>.service"}),"."]}),"\n"]}),"\n",(0,t.jsxs)(n.li,{children:["\n",(0,t.jsx)(n.p,{children:"Reload the systemd daemon:"}),"\n"]}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"systemctl daemon-reload\n"})}),"\n",(0,t.jsx)(n.h1,{id:"using-supervisor",children:"Using supervisor"}),"\n",(0,t.jsxs)(n.p,{children:["To run the bot on startup using ",(0,t.jsx)(n.code,{children:"supervisor"}),", you can follow the steps below:"]}),"\n",(0,t.jsxs)(n.ol,{children:["\n",(0,t.jsxs)(n.li,{children:["Install ",(0,t.jsx)(n.code,{children:"supervisor"}),":"]}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"sudo apt install supervisor\n"})}),"\n",(0,t.jsxs)(n.ol,{start:"2",children:["\n",(0,t.jsx)(n.li,{children:"Create a configuration file for your bot. You can use the following template:"}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-ini",children:"[program:<your bot name>]\ncommand=/home/user/your-user/venv/bin/python /path/to/bot.py\ndirectory=/path/to/bot/directory\nautostart=true\nautorestart=true\nstartsecs=10\nstderr_logfile=/var/log/<your bot name>.err.log\nstdout_logfile=/var/log/<your bot name>.out.log\n"})}),"\n",(0,t.jsxs)(n.ol,{start:"3",children:["\n",(0,t.jsxs)(n.li,{children:["\n",(0,t.jsxs)(n.p,{children:["Save the file as ",(0,t.jsx)(n.code,{children:"/etc/supervisor/conf.d/<your bot name>.conf"}),"."]}),"\n"]}),"\n",(0,t.jsxs)(n.li,{children:["\n",(0,t.jsx)(n.p,{children:"Reload the supervisor configuration:"}),"\n"]}),"\n"]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-bash",children:"sudo supervisorctl reread\nsudo supervisorctl update\n"})})]})}function h(e={}){const{wrapper:n}={...(0,o.R)(),...e.components};return n?(0,t.jsx)(n,{...e,children:(0,t.jsx)(c,{...e})}):c(e)}},8453:(e,n,s)=>{s.d(n,{R:()=>l,x:()=>i});var t=s(6540);const o={},r=t.createContext(o);function l(e){const n=t.useContext(r);return t.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function i(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(o):e.components||o:l(e.components),t.createElement(r.Provider,{value:n},e.children)}}}]);