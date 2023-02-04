# get_group_chat_history

Get the chat history of a channel or group.

## Signature

`async def get_group_chat_history(group_id:str, community_id: str, user_id:int =None, page_limit:int=100, page_offset:int=0) -> List[Message]:`


## Parameters

- `group_id` (str): The ID of the group
- `community_id` (str): The ID of the community
- `user_id` (int): The ID of the user
- `page_limit` (int): The maximum number of messages to return
- `page_offset` (int): The offset of the first message to return


:::tip
There is an analogous method for getting the chat history of a channel: [get_channel_chat_history](../methods/get_channel_chat_history).
:::


