# AppBar

The `AppBar` class represents an app bar in a user interface.

#### Properties

- `title` (Optional): The title of the app bar, default is "App".
- `subtitle` (Optional): The subtitle or additional information about the app bar.
- `left_icon` (Optional): The icon on the left side of the app bar. It can be either a string (URL) or an `Icon` component.
- `secondary_icon` (Optional): The secondary icon on the app bar. It can be either a string (URL) or an `Icon` component.
- `tertiary_icon` (Optional): The tertiary icon on the app bar. It can be either a string (URL) or an `Icon` component.

#### Methods

- **Constructor**

```python
def __init__(
    self,
    title: str = "App",
    subtitle: str = "",
    left_icon: Union[Icon, str] = Icon(...),
    secondary_icon: Union[Icon, str] = None,
    tertiary_icon: Union[Icon, str] = ""
)
```

#### Usage Example

```python
# Create an AppBar instance:
app_bar = AppBar(
    title="My App",
    subtitle="Subtitle Text",
    left_icon="https://raw.githubusercontent.com/switchcollab/Switch-Bots-Python-Library/main/docs/static/img/logo.png",
    secondary_icon="https://example.com/secondary-icon.png",
    tertiary_icon="https://example.com/tertiary-icon.png"
)
```