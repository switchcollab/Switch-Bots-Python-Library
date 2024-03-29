# Button
The `Button` class represents an action button in a user interface.

### Properties

- `text` (Required): The text content of the button. It can be either a string or a `Text` component.
- `icon` (Optional): The icon associated with the button. It can be either a string (URL) or an `Icon` component.
- `callback_data` (Optional): Data associated with a callback.

### Methods

- **Constructor**

```python
def __init__(
    self,
    text: Union[str, Text],
    icon: Union[str, Icon] = "",
    callback_data: Optional[str] = None,
)
```

### Usage Example

```python
# Create a Button instance:
button = Button(
    text="Click Me",
    icon="https://example.com/icon.png",
    callback_data="Callback Data"
)
```

## DownloadButton

Extends the `Button` class to represent a button with download functionality.

### Properties:

- `download_url`: The URL from which the file will be downloaded.
- `file_name`: The name to be given to the downloaded file.
- `text` (Optional): The text to be displayed on the button. Default is "Download". It can be a string or a `Text` object.
- `icon` (Optional): An icon associated with the button. It can be a string (URL) or an `Icon` component.
- `callback_data` (Optional): Callback data associated with the button.

### Constructor:

```python
def __init__(
    self,
    download_url: str,
    file_name: str,
    text: str | Text = "Download",
    icon: str | Icon = "",
    callback_data: str = None
)
```

### Usage Example:

```python
download_button = DownloadButton(
    download_url="https://example.com/file.zip",
    file_name="example_file.zip",
    text="Download File",
    icon="https://example.com/download-icon.png",
    callback_data="download_callback_data"
)
```

## ShareButton

Extends the `Button` class to represent a button with share functionality.

### Attributes:

- `text` (`str` or `Text`): The text content of the button.
- `share_text` (`str`): The text to be shared when the button is clicked.
- `icon` (`str` or `Icon`, optional): The icon associated with the button.
- `color` (`str`, optional): The color of the button.
- `variant` (`ButtonVariant`, optional): The variant of the button.

```python
def __init__(
    self,
    text: str | Text,
    icon: str | Icon = "",
    share_text: str = "",
    color: str = None,
    variant: ButtonVariant = ButtonVariant.DEFAULT,
)
```

### Usage Example:
```python
share_button = ShareButton(
    text="Share",
    share_text="Check out this awesome article!",
)
```

## ClipboardButton


### Attributes:

- `text` (`str` or `Text`): The text content of the button.
- `url` (`str`): The URL or text to be copied to the clipboard when the button is clicked.
- `icon` (`str` or `Icon`, optional): The icon associated with the button.
- `color` (`str`, optional): The color of the button.
- `variant` (`ButtonVariant`, optional): The variant of the button.

### Usage Example:
```python
clipboard_button = ClipboardButton(
    text="Copy Link",
    url="https://example.com/page",
)
```