# CommunityMember

`Class swibots.api.community.models.CommunityMember`

The `CommunityMember` class contains the info of the user linked with the community.

## Properties
- `id` (`int`): ID
- `admin` (`bool`): Is user admin.
- `username` (`str`): username of user.
- `user_id` (int): User Id of user.
- `community_id` (str): The community id.
- `user` ([User](./user.md)): The User Info.
- `xp` (int): The xp of the user.
- `xp_spend` (int): The xp spend by the user.
- `enable_notification` (`bool`): is User's notification are enabled.
- `role_info` (`dict`): the role info of user.
- `mute_period` (`str`): the mute period.
- `mute_notification` (`bool`):
- `mute_groups`: (`List[str]`): the muted groups.
- `mute_channels` (`List[str]`): the muted channels.