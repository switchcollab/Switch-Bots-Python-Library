# `get_organization_followers`
Retrieve the followers of a specific organization.

#### Signature:
```python
async def get_organization_followers(self: "swibots.ApiClient", id: str) -> List[User]:
```

#### Arguments:
- `id` (str): The ID of the organization.

#### Return Value:
- List[User]: A list of User objects representing followers.
