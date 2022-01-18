from __future__ import annotations

from typing import Any, Type

class Default: ...

def approx_equal(
    a1: Any,
    a2: Any,
    eps: float = ...,
    multiplier: float = ...,
    out: type[Default] = ...,
    prefix: str = ...,
) -> bool: ...
