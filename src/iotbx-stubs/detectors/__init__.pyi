from __future__ import annotations

from .adsc import ADSCImage
from .detectorbase import DetectorImageBase
from .edf import EDFImage

class SMVImage(ADSCImage):
    def __init__(self, filename: str) -> None: ...

class EDFWrapper(EDFImage, DetectorImageBase):
    def __init__(self, filename) -> None: ...
    def readHeader(self) -> None: ...  # type: ignore
