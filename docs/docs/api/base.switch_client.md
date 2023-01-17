<!-- markdownlint-disable -->

<a href="../../../src/switch/base/switch_client.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `base.switch_client`






---

<a href="../../../src/switch/base/switch_client.py#L10"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `SwitchRestClient`




<a href="../../../src/switch/base/switch_client.py#L11"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(base_url: str = None, token: str = None)
```






---

#### <kbd>property</kbd> base_url





---

#### <kbd>property</kbd> token







---

<a href="../../../src/switch/base/switch_client.py#L44"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `delete`

```python
delete(
    url: str,
    data: dict = None,
    headers: dict = None
) → RestResponse[Dict[str, Any]]
```

See :meth:`BaseRequest.delete`. 

---

<a href="../../../src/switch/base/switch_client.py#L81"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `do_request`

```python
do_request(
    path: str,
    method: str,
    data: dict = None,
    headers: dict = None
) → RestResponse[Dict[str, Any]]
```





---

<a href="../../../src/switch/base/switch_client.py#L32"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get`

```python
get(
    url: str,
    data: dict = None,
    headers: dict = None
) → RestResponse[Dict[str, Any]]
```

See :meth:`BaseRequest.get`. 

---

<a href="../../../src/switch/base/switch_client.py#L52"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `head`

```python
head(
    url: str,
    data: dict = None,
    headers: dict = None
) → RestResponse[Dict[str, Any]]
```

See :meth:`BaseRequest.head`. 

---

<a href="../../../src/switch/base/switch_client.py#L56"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `options`

```python
options(
    url: str,
    data: dict = None,
    headers: dict = None
) → RestResponse[Dict[str, Any]]
```

See :meth:`BaseRequest.options`. 

---

<a href="../../../src/switch/base/switch_client.py#L60"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `parse_response`

```python
parse_response(response: Tuple[int, bytes]) → RestResponse[Dict[str, Any]]
```





---

<a href="../../../src/switch/base/switch_client.py#L48"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `patch`

```python
patch(
    url: str,
    data: dict = None,
    headers: dict = None
) → RestResponse[Dict[str, Any]]
```

See :meth:`BaseRequest.patch`. 

---

<a href="../../../src/switch/base/switch_client.py#L36"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `post`

```python
post(
    url: str,
    data: dict = None,
    headers: dict = None
) → RestResponse[Dict[str, Any]]
```

See :meth:`BaseRequest.post`. 

---

<a href="../../../src/switch/base/switch_client.py#L72"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `prepare_request_data`

```python
prepare_request_data(data: dict) → dict
```





---

<a href="../../../src/switch/base/switch_client.py#L75"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `prepare_request_headers`

```python
prepare_request_headers(headers: dict) → dict
```





---

<a href="../../../src/switch/base/switch_client.py#L40"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `put`

```python
put(
    url: str,
    data: dict = None,
    headers: dict = None
) → RestResponse[Dict[str, Any]]
```

See :meth:`BaseRequest.put`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
