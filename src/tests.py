from swibots import BotApp, Message, BotContext, MessageEvent, MediaUploadRequest, CommandEvent, RegisterCommand# , EmbeddedMedia, EmbedInlineField


# print(MediaUploadRequest(""))
from swibots import BotInfo, Channel
app = BotApp(
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTczLCJpc19ib3QiOnRydWUsImFjdGl2ZSI6dHJ1ZSwiaWF0IjoxNjg5MTU5NTc1LCJleHAiOjIzMjAzMTE1NzV9.nehxRc3OrrHkcwCqCTs9uX3XaLpucnFYJWWaCHM1RIo"
)
import asyncio, logging
logging.basicConfig(level=logging.INFO)

@app.on_member_joined()
async def jo(e):
    print(e)

async def main():
    await app.start()
    print(app._token)
    print(await app.get_me())
    print(await app.get_referral(14))
    return
#    await app.get_members("")
    resp = await app.get_roles("30338819-7b57-4877-821f-b4ce2521614c")
#    app.
#    print(resp)

    #    rule = resp[0]

    for rule in resp:
#        ...
  #      print(rule.__dict__)
        print(rule.members_count, rule.name, rule.colour)
        print(await app.community_service.rolemember.get_members(rule.id))

        continue
        perm = await app.community_service.permission.get_permission(rule.id)
        print(perm.__dict__)
        me = await app.get_me()
#        me.id
        await app.community_service.permission.add_user_permission("30338819-7b57-4877-821f-b4ce2521614c", me.id, role_colour="Yellow", role_name="BOT", permission=RolePermission(
            add_members=True,
            send_messages=True
        ))
        if not perm:
            print(
                await app.community_service.permission.add_permission(
                    RolePermission(
                        add_members=True,
                        role_id=rule.id,
                        restrict_messaging=True,
                    )
                )
            )
    #    print(perm, perm.__dict__)
    #   perm.send_messages = False
    #  await app.community_service.permission.update_permission(perm)
    #    print(rule, rule.__dict__)
    #   await app.community_service.roles.delete_role(rule.id)
    return
    print(
        await app.community_service.roles.update_role(
            rule.community_id, rule.id, role_colour="green", role_name="Halle"
        )
    )


app._loop.run_until_complete(main())

exit()


@app.on_message()
async def priny(ctx):
    print(ctx.event.message.group)

@app.on_member_joined()
async def test(e):
    print(e)

@app.on_command("y")
async def message_handler(ctx: BotContext[CommandEvent]):
    # easy way to prepare a mesage that is a response of an incomming message
    print("sending message")
    return
    print(ctx.event.message_id)
    await ctx.event.message.forward_to("a1ea1639-335d-4251-9bd6-d33c94c84046")
    return
#    print(ctx.event.message)
   # userId = ctx.event.message.user.id
    #print(await app.get_community_member(ctx.event.message.community_id, userId))
    m = await ctx.prepare_response_message(ctx.event.message)
    m.message = f"Thank you! I received your message: {ctx.event.message.message}"
    # send the message back to the user
    m.status = 4  
    m.is_embed_message = "true"
    print(await ctx.send_message(m, EmbeddedMedia(description="Jo",
                                            header_icon="💝",
                                            footer_icon="💝",
                                            thumbnail=MediaUploadRequest("x.png"),
                                            title="Test",
                                            footer_title="OK",
                                            inline_fields=[[
                                            EmbedInlineField("👍", "2", "OK")
                                            ]])))

app.register_command([
    RegisterCommand("y","ok", True)
])
app.run()
