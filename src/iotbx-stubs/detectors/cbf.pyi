from __future__ import annotations

from typing import Any

from .detectorbase import DetectorImageBase
from .marIP import MARIPImage

class CBFImage(MARIPImage):
    adaptor: Any
    vendortype: str
    vendor_specific_null_value: Any
    def __init__(self, filename) -> None: ...
    def beam_center_slow(self): ...
    def beam_center_fast(self): ...
    def read(self) -> None: ...
