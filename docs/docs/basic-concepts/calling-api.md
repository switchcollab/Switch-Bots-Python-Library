---
sidebar_position: 2
---

# Calling the API methods

After your [project is set up](./project-setup), you can start creating your app
and calling the API methods

## Basic usage

Making API calls with SwiBots is very simple. Here’s a basic example we are going to examine step by step:

```python
from swibots import BotApp

app = BotApp("TOKEN")

async def main():
    async with app:
        me = await app.get_me()
        print(me)

app.run(main())
```

## Step by step

1. Import the BotApp from swibots, you will import all your classes from this package

```python
from swibots import BotApp
```

2. Instantiate the class with your TOKEN

```python
app = BotApp("TOKEN")
```

3. Async methods must be invoked within an async context. Here we define an async function and put our code inside. Also notice the `await` keyword in front of the method call; this is required for all asynchronous methods.

```python
async def main():
    async with app:
        me = await app.get_me()
        print(me)
```

4. Finally, we tell Python to schedule our main() async function by using BotApp run() method.

```python
app.run(main())
```


## Context Manager
The async with statement starts a context manager, which is used as a shortcut for starting, executing and stopping the App, asynchronously. It does so by automatically calling `start()` and `stop()` in a more convenient way which also gracefully stops the app, even in case of unhandled exceptions in your code.

Below there’s the same example as above, but without the use of the context manager:

```python
from swibots import BotApp

app = BotApp("TOKEN")


async def main():
    await app.start()
    me = await app.get_me()
    print(me)
    await app.stop()


app.run(main())
```

## Using asyncio.run()

Alternatively to the run() method, you can use Python’s asyncio.run() to execute the main function, with one little caveat: the App instance (and possibly other asyncio resources you are going to use) must be instantiated inside the main function.

```python
import asyncio
from swibots import BotApp

async def main():
    app = BotApp("TOKEN")
    async with app:
        me = await app.get_me()
        print(me)

asyncio.run(main())
```