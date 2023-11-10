# `get_organization_apps`

Retrieve the apps associated with a specific organization.

#### Signature:
```python
async def get_organization_apps(self: "swibots.ApiClient", id: str) -> List[OrgApp]:
```

#### Arguments:
- `id` (str): The ID of the organization.

#### Return Value:
- List[OrgApp]: The OrgApp object.
