# get_channel_chat_history

Get the chat history of a channel or group.

## Signature

`async def get_channel_chat_history(channel_id:str, community_id: str, user_id:int =None, page_limit:int=100, page_offset:int=0) -> List[Message]:`


## Parameters

- `channel_id` (str): The ID of the channel
- `community_id` (str): The ID of the community
- `user_id` (int): The ID of the user
- `page_limit` (int): The maximum number of messages to return
- `page_offset` (int): The offset of the first message to return


:::tip
There is an analogous method for getting the chat history of a group: [get_group_chat_history](../methods/get_group_chat_history).
:::


