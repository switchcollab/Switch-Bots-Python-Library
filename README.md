<p align="center">
  <img src="https://raw.githubusercontent.com/switchcollab/Switch-Bots-Python-Library/main/docs/static/img/switch-logo.png" alt="Logo">
</p>

![GitHub stars](https://img.shields.io/github/stars/switchcollab/Switch-Bots-Python-Library)
![GitHub Forks](https://img.shields.io/github/forks/switchcollab/Switch-Bots-Python-Library)
![Version](https://img.shields.io/badge/version-0.3.30-teal.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/swibots)

# SwiBots: Python Library for Switch App

SwiBots is a Python library designed to simplify the development of apps for the
Switch platform. With SwiBots, you can create interactive and engaging bots for
the Switch app effortlessly.

For detailed information and documentation, please visit our
[documentation website](https://switchcollab.github.io/Switch-Bots-Python-Library).

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage example](#usage-example)
- Quick Guide
  - [Embedded message](#sending-embedded-messages)
  - [Sending media](#sending-media)
  - [Sending buttons](#sending-buttons)
- [More samples](#explore-bot-samples)
- [Code Contribution](#🚀-contributing)

## Getting Started

You can start building your first app with SwiBots in less than 5 minutes.

### Installation

To install SwiBots, you can use pip:

```bash
pip install swibots
```

Alternatively, you can install it from the GitHub repository:

```bash
pip install git+https://github.com/switchcollab/Switch-Bots-Python-Library.git
```

### Usage Example

Let's create a simple echo bot to get you started quickly. Follow these steps:

1. Create a Python file, e.g., `echobot.py`.

2. Add the following code to your `echobot.py` file:

```python
from swibots import (
    BotApp,
    BotContext,
    MessageEvent
)

TOKEN = "MY SUPER SECRET TOKEN"

# Initialize the app and register commands
app = BotApp(
    TOKEN, "A cool bot with annotations and everything you could possibly want :)"
)

@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
    # Easy way to prepare a message that is a response to an incoming message
    message = ctx.event.message
    response_text = f"Thank you! I received your message: {message.message}"
    # Send the message back to the user
    await message.respond(response_text)

app.run()
```

3. Open your Switch app and send a message to the bot, e.g., `Hello world!`

4. Your bot will reply with: `Thank you! I received your message: Hello world!`

### Explore Bot Samples

For more examples and sample bots, please check out our [Bot samples](./samples)
directory.

## Examples

### Sending Buttons

You can easily send interactive buttons in your messages using SwiBots:

```python
from swibots import InlineMarkup, InlineKeyboardButton

await bot.send_message(
    message="Hi",
    user_id=bot.user.id,
    inline_markup=InlineMarkup([[
        InlineKeyboardButton("Click Me", url="https://example.com")
    ]])
)
```

### Sending Media

Sending media files with your messages is a breeze:

```python
await bot.send_media(
    message="This is a message",
    user_id=100,
    document="file.pdf",
    description="file_name.png",
    thumbnail="file.png"
)
```

### Sending Embedded Messages

You can create visually appealing embedded messages with SwiBots:

```python
from swibots import EmbeddedMedia, EmbedInlineField

await bot.send_message(
    message="Embedded message",
    user_id=400,
    media=EmbeddedMedia(
        thumbnail="thumb_path.png",
        title="Embedded message.",
        header_name="Message from SwiBots!",
        header_icon="https://header.png",
        footer_title="Hello from the bot.",
        footer_icon="https://footer.png",
        inline_fields=[
            [
                EmbedInlineField("https://icon.png", "Nice Meeting You", "Hello 👋")
            ]
        ]
    )
)
```

Feel free to explore more features and capabilities of SwiBots in our
documentation.

Happy bot development!

## 🚀 Contributing

Thank you for considering contributing to SwiBots! We welcome your contributions
to make this project even better.

1. 🧐 **Check for Existing Issues**: Look for existing issues or feature
   requests before starting.

2. 🐞 **Report a Bug or Request a Feature**: If you find a bug or have an idea,
   [create an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)
   with details.

3. 🛠️ **Submit a Pull Request (PR)**: For code changes, follow our
   [PR guidelines](#pull-request-guidelines) and
   [create a PR](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

We appreciate your contributions and look forward to your help in improving
SwiBots! 🙌
