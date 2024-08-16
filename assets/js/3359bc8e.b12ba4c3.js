"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[7577],{1106:(e,n,s)=>{s.r(n),s.d(n,{assets:()=>l,contentTitle:()=>a,default:()=>p,frontMatter:()=>r,metadata:()=>o,toc:()=>c});var i=s(5893),t=s(1151);const r={sidebar_position:3},a="Inline queries",o={id:"interactions/inline_queries",title:"Inline queries",description:"Switch supports inline queries. This means that you can send a query to a bot and receive a list of results from it. This is useful for things like searching for a specific item in a database, or getting a list of results from an API.",source:"@site/docs/interactions/inline_queries.md",sourceDirName:"interactions",slug:"/interactions/inline_queries",permalink:"/Switch-Bots-Python-Library/docs/interactions/inline_queries",draft:!1,unlisted:!1,tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"tutorialSidebar",previous:{title:"Advertising",permalink:"/Switch-Bots-Python-Library/docs/interactions/advertising"},next:{title:"Callback queries",permalink:"/Switch-Bots-Python-Library/docs/interactions/callback_queries"}},l={},c=[{value:"Inline query basics",id:"inline-query-basics",level:2},{value:"Inline query example",id:"inline-query-example",level:2}];function u(e){const n={a:"a",code:"code",h1:"h1",h2:"h2",p:"p",pre:"pre",...(0,t.a)(),...e.components};return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(n.h1,{id:"inline-queries",children:"Inline queries"}),"\n",(0,i.jsx)(n.p,{children:"Switch supports inline queries. This means that you can send a query to a bot and receive a list of results from it. This is useful for things like searching for a specific item in a database, or getting a list of results from an API."}),"\n",(0,i.jsx)(n.h2,{id:"inline-query-basics",children:"Inline query basics"}),"\n",(0,i.jsxs)(n.p,{children:["Every time a user types ",(0,i.jsx)(n.code,{children:"@botname"})," in a chat, the bot will receive an ",(0,i.jsx)(n.code,{children:"inline_query"})," event. This event contains the query string and the context of where the user is using the inline query."]}),"\n",(0,i.jsx)(n.p,{children:"The bot can send a response to the user's inline query. This response is a list of results. Each result can be an article, a photo, a video or document."}),"\n",(0,i.jsxs)(n.p,{children:["Please refer to the ",(0,i.jsx)(n.a,{href:"/docs/api_reference/types/inline/inline_query_answer",children:"InlineQueryAnswer"})," class for more information about the available inline query result types."]}),"\n",(0,i.jsx)(n.h2,{id:"inline-query-example",children:"Inline query example"}),"\n",(0,i.jsx)(n.p,{children:"Here is an example of how to handle an inline query:"}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",children:'\nimport logging\nimport json\nfrom typing import Tuple\nfrom swibots import Client, BotContext, MessageEvent, Message, InlineQuery, InlineQueryEvent, RestClient, RestResponse, JSONDict, NetworkError, InlineQueryResultArticle, InputMessageContent\n\nlogging.basicConfig(level=logging.INFO)\n\nlog = logging.getLogger(__name__)\n\nrestclient = RestClient()\n\ndef parse_response(response: Tuple[int, bytes]) -> RestResponse[JSONDict]:\n    decoded_s = response[1].decode("utf-8", "replace")\n    try:\n        jsonObject = json.loads(decoded_s)\n    except ValueError as exc:\n        jsonObject = decoded_s\n\n    response = RestResponse(jsonObject, response[0], {})\n    if response.is_error:\n        raise NetworkError(response.error_message)\n    return response\n\n\nTOKEN = "your_token"\n\napp = Client(TOKEN, "This is an inline query bot")\n\n@app.on_message()\nasync def on_message(ctx: BotContext[MessageEvent]):\n    message: Message = ctx.event.message\n    log.info(f"Message: {message.message}")\n    await message.reply_text(f"Echo: {message.message}")\n\n\n@app.on_inline_query()\nasync def on_inline_query(ctx: BotContext[InlineQueryEvent]):\n    query: InlineQuery = ctx.event.query\n    log.info(f"Inline query: {query.query}")\n    await query.answer(f"Searching results for {query.query}...")\n    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search={query.query}&limit=50"\n    response = parse_response(await restclient.get(url))\n    if response.status_code == 200:\n        data = response.data\n        results = []\n        for i in range(len(data[1])):\n            results.append(\n                InlineQueryResultArticle(\n                    id=str(i),\n                    title=data[1][i],\n                    description=data[1][i],\n                    input_message=InputMessageContent(data[2][i]),\n                    article_url=data[3][i],\n                    thumb_url=\n                    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png",\n                    thumb_width=48,\n                    thumb_height=48,\n                )\n            )\n        await query.answer(results)\n    else:\n        await query.answer("There was an error while searching for results.")\n\n\napp.run()\n'})})]})}function p(e={}){const{wrapper:n}={...(0,t.a)(),...e.components};return n?(0,i.jsx)(n,{...e,children:(0,i.jsx)(u,{...e})}):u(e)}},1151:(e,n,s)=>{s.d(n,{Z:()=>o,a:()=>a});var i=s(7294);const t={},r=i.createContext(t);function a(e){const n=i.useContext(r);return i.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function o(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(t):e.components||t:a(e.components),i.createElement(r.Provider,{value:n},e.children)}}}]);