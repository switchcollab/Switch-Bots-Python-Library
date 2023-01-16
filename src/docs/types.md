<!-- markdownlint-disable -->

<a href="../../src/switch/types.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `types`
Define names for built-in types that aren't directly accessible as a builtin. 


---

<a href="../../src/types/new_class#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `new_class`

```python
new_class(name, bases=(), kwds=None, exec_body=None)
```

Create a class object dynamically using the appropriate metaclass. 


---

<a href="../../src/types/resolve_bases#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `resolve_bases`

```python
resolve_bases(bases)
```

Resolve MRO entries dynamically as specified by PEP 560. 


---

<a href="../../src/types/prepare_class#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `prepare_class`

```python
prepare_class(name, bases=(), kwds=None)
```

Call the __prepare__ method of the appropriate metaclass. 

Returns (metaclass, namespace, kwds) as a 3-tuple 

*metaclass* is the appropriate metaclass *namespace* is the prepared class namespace *kwds* is an updated copy of the passed in kwds argument with any 'metaclass' entry removed. If no kwds argument is passed in, this will be an empty dict. 


---

<a href="../../src/types/coroutine#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `coroutine`

```python
coroutine(func)
```

Convert regular generator function to a coroutine. 


---

<a href="../../src/switch/types.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `DynamicClassAttribute`
Route attribute access on a class to __getattr__. 

This is a descriptor, used to define attributes that act differently when accessed through an instance and through a class.  Instance access remains normal, but access to an attribute through a class will be routed to the class's __getattr__ method; this is done by raising AttributeError. 

This allows one to have properties active on an instance, and have virtual attributes on the class with the same name.  (Enum used this between Python versions 3.4 - 3.9 .) 

Subclass from this to use a different method of accessing virtual attributes and still be treated properly by the inspect module. (Enum uses this since Python 3.10 .) 

<a href="../../src/types/__init__#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(fget=None, fset=None, fdel=None, doc=None)
```








---

<a href="../../src/types/deleter#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `deleter`

```python
deleter(fdel)
```





---

<a href="../../src/types/getter#L193"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `getter`

```python
getter(fget)
```





---

<a href="../../src/types/setter#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setter`

```python
setter(fset)
```






---

<a href="../../src/switch/types.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GenericAlias`
Represent a PEP 585 generic type 

E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,). 





---

<a href="../../src/switch/types.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SimpleNamespace`
A simple attribute-based namespace. 

SimpleNamespace(**kwargs) 





---

<a href="../../src/switch/types.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `UnionType`
Represent a PEP 604 union type 

E.g. for int | str 





---

<a href="../../src/switch/types.py#L4"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventType`
Represents the type of a event. 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
