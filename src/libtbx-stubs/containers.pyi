from collections.abc import Collection, Iterator, MutableSet
from typing import Any, Dict, List, Optional, Type

class OrderedSet(MutableSet):
    end: List[Any]
    map: Dict
    def __init__(self, iterable: Optional[Collection] = ...) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> Iterator[Any]: ...
    def add(self, key: Any) -> None: ...
    def discard(self, key: Any) -> None: ...
    def pop(self, last: bool = ...): ...

class deque_template:
    def __init__(self) -> None: ...
    def push(self, item): ...
    def __bool__(self): ...
    def __contains__(self, item): ...

class stack(deque_template):
    list_proxy_type: Type
    set_proxy_type: Optional[Type]
    def pull(self): ...

class hashed_stack(stack):
    set_proxy_type: Type

class queue(deque_template):
    list_proxy_type: Optional[Type]
    set_proxy_type: Optional[Type]
    def pull(self): ...

class hashed_queue(queue):
    set_proxy_type: Type
