---
sidebar_position: 5
---

# Games
Games on the are the termed referred to the web game (HTML5, any).

```python
from swibots import BotApp, InlineKeyboardButton, InlineMarkup

app = BotApp('TOKEN')

await app.send_message(
    message="Hi",
    user_id=100,
    inline_markup=InlineMarkup([
        [InlineKeyboardButton(text="Play Game", game=True)]
    ])
)
```

## Leaderboards
- User is allowed to have 2 classification, (one for the private chats, and other per each community.)

### Creating leaderboard
```python
await app.create_leaderboard(
    user_id=user_id,
    community_id=community_id,
    score=score
)
```

### Getting Global leaderboard
```python
await app.get_global_leaderboard()
```

### Getting Community leaderboard
```python
await app.get_community_leaderboard(
    community_id=communityId
)
```

### Getting User's score
```python
await app.get_game_score(
    user_id=user_id,
    community_id=communityId
    # ignore community id to get score in user's private
)
```
