# Text

The `Text` class represents text in a user interface.

#### Properties

- `text` (Required, `str`): The text content.
- `size` (Optional, `TextSize`): The size of the text, default is `TextSize.BODY`.
- `opacity` (Optional): The opacity of the text, default is `1`.

#### Usage Example

```python
# Create a Text instance:
text_component = Text(text="Hello, World!", size=TextSize.HEADER, opacity=0.8)
```

## TextSize

The `TextSize` enumeration defines different sizes for text in a user interface.

#### Values

- `SMALL`: Represents small text size.
- `MEDIUM`: Represents medium text size.
- `LARGE`: Represents large text size.
- `BODY`: Represents the default body text size.
- `BOLD`: Represents bold body text size.
- `MARKDOWN`: Represents text size for Markdown content.
