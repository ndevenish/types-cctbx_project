from __future__ import annotations

from typing import Any

header_struct: Any

class Raxis:
    file: Any
    head: Any
    CharTemp: Any
    def __init__(self, file) -> None: ...
    def readHeader(self, verbose: int = ...) -> None: ...
    def data(self) -> None: ...
    def dump(self) -> None: ...
