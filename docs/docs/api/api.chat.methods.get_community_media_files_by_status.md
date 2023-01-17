<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_community_media_files_by_status.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.get_community_media_files_by_status`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_community_media_files_by_status.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetCommunityMediaFilesByStatus`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_community_media_files_by_status.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_community_media_files_by_status`

```python
get_community_media_files_by_status(
    self: 'ApiClient',
    community_id: str,
    status: str
) → List[Message]
```

Get community media files by status 



**Parameters:**
 
 - <b>`community_id`</b> (``int``):  The community id 
 - <b>`status`</b> (``str``):  The status 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be retrieved 

This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_community_media_files_by_status`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
