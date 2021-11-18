from typing import Any, Type

class Default: ...

def approx_equal(
    a1: Any,
    a2: Any,
    eps: float = ...,
    multiplier: float = ...,
    out: Type[Default] = ...,
    prefix: str = ...,
) -> bool: ...
