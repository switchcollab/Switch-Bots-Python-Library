<!-- markdownlint-disable -->

<a href="../../../src/switch/bots/filters/filter.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `bots.filters.filter`




**Global Variables**
---------------
- **CUSTOM_FILTER_NAME**
- **all**
- **self**
- **is_bot**
- **me**
- **incoming**
- **outgoing**
- **community**
- **channel**
- **group**
- **user**

---

<a href="../../../src/switch/bots/filters/filter.py#L66"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `create`

```python
create(
    func: Callable[[~CtxType], Coroutine[Any, Any, bool]],
    name: str = None,
    **kwargs
) → Filter
```






---

<a href="../../../src/switch/bots/filters/filter.py#L72"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `all_filter`

```python
all_filter(ctx: BotContext)
```






---

<a href="../../../src/switch/bots/filters/filter.py#L80"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `self_filter`

```python
self_filter(ctx: BotContext[MessageEvent])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L91"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `bot_filter`

```python
bot_filter(ctx: BotContext[MessageEvent])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L101"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `me_filter`

```python
me_filter(ctx: BotContext[MessageEvent])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L109"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `incoming_filter`

```python
incoming_filter(ctx: BotContext[MessageEvent])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L117"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `outgoing_filter`

```python
outgoing_filter(ctx: BotContext[MessageEvent])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L125"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `community_filter`

```python
community_filter(
    ctx: BotContext[Event],
    community_id: Optional[str, Collection[str]]
)
```






---

<a href="../../../src/switch/bots/filters/filter.py#L139"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `channel_filter`

```python
channel_filter(
    ctx: BotContext[Event],
    channel_id: Optional[str, Collection[str]]
)
```






---

<a href="../../../src/switch/bots/filters/filter.py#L153"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `group_filter`

```python
group_filter(ctx: BotContext[Event], group_id: Optional[str, Collection[str]])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L167"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `user_filter`

```python
user_filter(ctx: BotContext[Event], user_id: Optional[str, Collection[str]])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L181"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `text`

```python
text(text: Optional[str, Collection[str]])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L214"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>function</kbd> `regex_filter`

```python
regex_filter(regexp: Optional[str, Collection[str]])
```






---

<a href="../../../src/switch/bots/filters/filter.py#L11"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `Filter`








---

<a href="../../../src/switch/bots/filters/filter.py#L25"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `InvertFilter`




<a href="../../../src/switch/bots/filters/filter.py#L26"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(base)
```









---

<a href="../../../src/switch/bots/filters/filter.py#L34"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `AndFilter`




<a href="../../../src/switch/bots/filters/filter.py#L35"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(base, other)
```









---

<a href="../../../src/switch/bots/filters/filter.py#L49"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `OrFilter`




<a href="../../../src/switch/bots/filters/filter.py#L50"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(base, other)
```











---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
