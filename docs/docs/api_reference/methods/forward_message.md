# forward_message

Forwards a message to a user, channel or group.

# Signature

`async def  forward_message(message: Message | int,group_channel: Group | Channel | str = None,receiver_id: int = None) -> Message`

# Parameters

- `message` (`Message` | `int`): The message to forward or its ID
- `group_channel` Optional (`Group` | `Channel`| `str`, Optional): The group or channel to forward the message to (or its ID)
- `receiver_id` Optional (`int`): The ID of the user to forward the message to


- > Specify group_channel to forward message to the group or channel
- > and receiver_id to forward to the user.