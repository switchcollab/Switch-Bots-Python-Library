import asyncio
from switch.api.chat.models.message import Message
from switch.api.switch_client import SwitchClient
import logging


logging.basicConfig(level=logging.DEBUG)

async def main():
    client=SwitchClient()
    await client.initialize()
    client.token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjM1LCJpc19ib3QiOnRydWUsImFjdGl2ZSI6dHJ1ZSwiaWF0IjoxNjcyMzM3MDc3LCJleHAiOjE2NzM1NDY2Nzd9.vqLqQ0M5yQFkIWwDh9k38oIfh8TFItywWJoMoS3iYcY"
    # messages= await client.chat.messages().get_messages()
    # print(messages[0].message)
    # message= await client.chat.messages().send_message(Message(userId=235, receiverId=10, message="Hello World"))
    # print(message.message)
    user = await client.auth.users().get_user()
    print(user.username)


if __name__ == "__main__":
    asyncio.run(main())