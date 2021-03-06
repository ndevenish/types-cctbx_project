from __future__ import annotations

from typing import Any

from .detectorbase import DetectorImageBase

class ADSCHF4MImage(DetectorImageBase):
    vendortype: str
    vendor_specific_null_value: int
    mandatory_keys: Any
    adaptor: Any
    header: Any
    headerlines: Any
    parameters: Any
    def __init__(self, filename) -> None: ...
    def fileLength(self) -> None: ...
    def getEndian(self) -> None: ...
    def endian_swap_required(self): ...
    def read(self, algorithm: str = ...) -> None: ...
    def readHeader(self, maxlength: int = ...) -> None: ...
