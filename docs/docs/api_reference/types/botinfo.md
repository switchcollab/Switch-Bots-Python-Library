# BotInfo

`Class swibots.api.bot.models.BotInfo`

The `BotInfo` class contain information of bot profile.


# Parameters
- `id` (`str`): the bot id
- `name` (`str`): the name of bot.
- `description` (`str`): the description of profile.
- `username` (`str`): the username.
- `image_url` (`str`): the url to the bot profile photo.
- `active` (`bool`): whether bot is active.
- `deleted` (`bool`): if profile is deleted.
- `is_bot` (`bool`): if profile belongs to bot.
- `commands` (`List[BotCommandInfo]`): the list of bot commands.
- `role_info` (`str`): the role info.
