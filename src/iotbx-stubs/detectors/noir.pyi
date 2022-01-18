from __future__ import annotations

from typing import Any

from .adsc import ADSCImage

class NoirImage(ADSCImage):
    vendortype: str
    header: Any
    parameters: Any
    def __init__(self, filename) -> None: ...
    def getTupleofType(self, inputstr, typefunc): ...
    def readHeader(self, maxlength: int = ...) -> None: ...  # type: ignore
    def read(self) -> None: ...
