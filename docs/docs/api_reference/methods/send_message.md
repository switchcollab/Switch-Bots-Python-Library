# send_message

Send a text message to a user, channel or group.

## Signature

```python
async def send_message(
    message: str,
    community_id: Optional[str] = None,
    channel_id: Optional[str] = None,
    group_id: Optional[str] = None,
    user_id: Optional[int] = None,
    embed_message: Optional[EmbeddedMedia] = None,
    inline_markup: InlineMarkup = None,
   ) -> Message:
```

## Parameters

- `message` (`str`): The message to send
- `community_id` (`str`): The community id to send message.
- `group_id` (`str`): The Group ID.
- `channel_id` (`str`): Channel ID.
- `user_id` (`int`): User ID to send message.
- `embed_message` ([EmbeddedMedia](../types/embedded_media.md)).
- `inline_markup` ([InlineMarkup](../types/inline_markup.md)): Inline Markup linked with message.