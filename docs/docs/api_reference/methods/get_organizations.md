# `get_organizations`
Retrieve a list of organizations based on specified parameters.

#### Signature:
```python
async def get_organizations(
    self,
    bot_id: int = None,
    community_id: str = None,
    user_id: str = None,
) -> List[Organization]:
```

#### Arguments:
- `bot_id` (int, optional): The ID of the bot associated with the organizations.
- `community_id` (str, optional): The ID of the community associated with the organizations.
- `user_id` (str, optional): The ID of the user associated with the organizations.

#### Return Value:
- List[Organization]: A list of Organization objects.
