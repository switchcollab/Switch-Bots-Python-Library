<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_user_media_files.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.get_user_media_files`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_user_media_files.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetUserMediaFiles`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_user_media_files.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_user_media_files`

```python
get_user_media_files(self: 'ApiClient', user_id: int = None) → List[Message]
```

Get user media files 





**Parameters:**
 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The user media files 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the user media files could not be retrieved 

This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_user_media_files`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
