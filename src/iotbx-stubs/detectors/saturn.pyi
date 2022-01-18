from __future__ import annotations

from typing import Any, Dict, Type

from iotbx.detectors.adsc import ADSCImage as ADSCImage

class SaturnImage(ADSCImage):
    header: str
    parameters: dict[str, Any]
    vendortype: str
    def __init__(self, filename) -> None: ...
    def getTupleofType(self, inputstr: str, typefunc: type): ...
    def read(self) -> None: ...
    def readHeader(self, maxlength: int = ...) -> None: ...  # type: ignore # this does not match parent declaration
