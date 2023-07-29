# deduct_xp

Deduct the XP of user.

## Signature

`async def deduct_xp(community_id: str, user_id: int, xp: int, description: str = None) -> Channel`

## Parameters
- `community_id` (`str`): The ID of the community.
- `user_id` (`int`): The ID of the user.
- `xp` (`int`): The amount of XP to deduct.
- `description` (`str`): An optional description of the reason for the deduction.