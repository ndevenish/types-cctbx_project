from __future__ import annotations

from typing import Any

from .raxis import RAXISImage

class NonSquareRAXISImage(RAXISImage):
    np: Any
    extra: Any
    rawlinearintdata: Any
    def __init__(self, filename) -> None: ...
    def readHeader(self) -> None: ...  # type: ignore
    def generic_param_from_adapt_head(self) -> None: ...
    def read(self) -> None: ...
