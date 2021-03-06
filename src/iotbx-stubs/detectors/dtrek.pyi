from __future__ import annotations

from typing import Any

from .detectorbase import DetectorImageBase

verbose: bool

class DTREKImage(DetectorImageBase):
    vendortype: str
    def __init__(self, filename) -> None: ...
    header: Any
    headerlines: Any
    keys: Any
    def read_vendor_header(self) -> None: ...
    enf: Any
    def enforce_types(self) -> None: ...
    def tokenize(self, string_): ...
    parameters: Any
    def generic_param_from_vendor_head(self) -> None: ...
    def readHeader(self) -> None: ...
    def getEndian(self): ...
    def read(self) -> None: ...
