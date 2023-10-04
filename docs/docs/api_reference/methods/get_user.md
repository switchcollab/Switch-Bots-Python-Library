# get_user

 get the [User](../types/user.md) info from user id.

## Signature

`async def get_user(user_id: int=None, username: str = None) -> User`

## Parameters

- `user_id` (int): The ID of the user to get info.
- `username` (str): username

## Raises
- ValueError: if both user_id and username are used.