# edit_message

Edits a message

# Signature

```python
async def edit_message(
        self,
        message_id: int,
        text: str,
        embed_message: EmbeddedMedia = None,
        inline_markup: InlineMarkup = None,
        **kwargs)-> Message:
```

# Parameters

- `message` ([Message](../types/message)): The message to edit (if the message has not ID, it will be sent as a new message)
