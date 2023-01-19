---
sidebar_position: 1
---

# Project setup

You have learned how to create a very [basic bot](../intro) in the Quick start guide. In this page we will discuss
how to configure the project to properly create your bots

# Auth Key

You will need an AuthKey to use PySwitch, you can obtain your key on the Switch app

:::danger
Never share your AuthKey or commit it to any source code versioning system!
:::

# Configuration

Having the API key from the previous step, we can now begin to configure a PySwitch project: pass your API key to PySwitch by using the token parameter of the BotApp class:

```python
from pyswitch import BotApp

TOKEN = "MY SUPER SECRET TOKEN"

# initialize the app
app = BotApp(
    TOKEN
)
```