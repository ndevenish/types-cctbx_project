from typing import Any, Dict, Type

from iotbx.detectors.adsc import ADSCImage as ADSCImage

class SaturnImage(ADSCImage):
    header: str
    parameters: Dict[str, Any]
    vendortype: str
    def __init__(self, filename) -> None: ...
    def getTupleofType(self, inputstr: str, typefunc: Type): ...
    def read(self) -> None: ...
    def readHeader(self, maxlength: int = ...) -> None: ...  # type: ignore # this does not match parent declaration
