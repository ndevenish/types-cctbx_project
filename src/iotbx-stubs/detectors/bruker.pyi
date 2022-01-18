from __future__ import annotations

from typing import Any

from .detectorbase import DetectorImageBase

class BrukerImage(DetectorImageBase):
    filename: Any
    bruker: Any
    bin: int
    vendortype: str
    def __init__(self, filename) -> None: ...
    parameters: Any
    def readHeader(self) -> None: ...
    def read(self) -> None: ...
