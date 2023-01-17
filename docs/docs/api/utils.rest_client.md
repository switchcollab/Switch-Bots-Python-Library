<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `utils.rest_client`




**Global Variables**
---------------
- **DEFAULT_HEADERS**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L17"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `RestClient`




<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L18"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    connection_pool_size: int = 1,
    proxy_url: str = None,
    read_timeout: Optional[float] = 5.0,
    write_timeout: Optional[float] = 5.0,
    connect_timeout: Optional[float] = 5.0,
    pool_timeout: Optional[float] = 1.0
)
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L82"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `delete`

```python
delete(url: str, data: dict = None, headers: dict = None) → Tuple[int, bytes]
```

See :meth:`BaseRequest.delete`. 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L110"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `do_request`

```python
do_request(
    url: str,
    method: str,
    data: dict = None,
    headers: dict = None
) → Tuple[int, bytes]
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L70"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get`

```python
get(url: str, data: dict = None, headers: dict = None) → Tuple[int, bytes]
```

See :meth:`BaseRequest.get`. 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L90"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `head`

```python
head(url: str, data: dict = None, headers: dict = None) → Tuple[int, bytes]
```

See :meth:`BaseRequest.head`. 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L58"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `initialize`

```python
initialize() → None
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L94"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `options`

```python
options(url: str, data: dict = None, headers: dict = None) → Tuple[int, bytes]
```

See :meth:`BaseRequest.options`. 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L126"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `parse_json_payload`

```python
parse_json_payload(payload: bytes) → Dict[str, Any]
```

Parse the JSON returned from Switch. Tip:  By default, this method uses the standard library's :func:`json.loads` and  ``errors="replace"`` in :meth:`bytes.decode`.  You can override it to customize either of these behaviors. 

**Args:**
 
 - <b>`payload`</b> (:obj:`bytes`):  The UTF-8 encoded JSON payload as returned by Telegram. 

**Returns:**
 
 - <b>`dict`</b>:  A JSON parsed as Python dict with results. 

**Raises:**
 
 - <b>`SwitchError`</b>:  If loading the JSON data failed 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L86"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `patch`

```python
patch(url: str, data: dict = None, headers: dict = None) → Tuple[int, bytes]
```

See :meth:`BaseRequest.patch`. 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L74"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `post`

```python
post(url: str, data: dict = None, headers: dict = None) → Tuple[int, bytes]
```

See :meth:`BaseRequest.post`. 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L100"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `prepare_request_data`

```python
prepare_request_data(data: dict) → str | None
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L104"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `prepare_request_headers`

```python
prepare_request_headers(headers: dict) → dict
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L78"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `put`

```python
put(url: str, data: dict = None, headers: dict = None) → Tuple[int, bytes]
```

See :meth:`BaseRequest.put`. 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/utils/rest_client.py#L63"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `shutdown`

```python
shutdown() → None
```

See :meth:`BaseRequest.shutdown`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
