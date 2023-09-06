# send_media

Send a message with media to a user, channel or group.

## Signature

```python
async def send_media(
    message: str,
    document: str,
    community_id: Optional[str] = None,
    channel_id: Optional[str] = None,
    group_id: Optional[str] = None,
    user_id: Optional[int] = None,
    embed_message: Optional[EmbeddedMedia] = None,
    inline_markup: InlineMarkup = None,
    scheduled_at: Optional[int] = None
    **kwargs
   ) -> Message:
```

## Parameters

- `message` (`str`): The message to send
- `document` (`str`): Path to file
- `community_id` (`str`): The community id to send message.
- `group_id` (`str`): The Group ID.
- `channel_id` (`str`): Channel ID.
- `user_id` (`int`): User ID to send message.
- `embed_message` ([EmbeddedMedia](../types/embedded_media.md)).
- `inline_markup` ([InlineMarkup](../types/inline_markup.md)): Inline Markup linked with message.
- `scheduled_at` (`int`): timestamp to schedule message.