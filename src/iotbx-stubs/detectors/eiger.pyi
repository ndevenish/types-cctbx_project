from __future__ import annotations

from typing import Any

from .detectorbase import DetectorImageBase

vendortype_from_size: Any

class EIGERImage(DetectorImageBase):
    vendortype: str
    supports_multiple_images: bool
    img_number: Any
    vendor_specific_null_value: int
    mandatory_keys: Any
    parameters: Any
    zero_oscillation: Any
    image_size_fast: Any
    image_size_slow: Any
    pixel_resolution: Any
    def __init__(self, filename, index: int = ...) -> None: ...
    def readHeader(self, dxtbx_instance, maxlength: int = ...) -> None: ...
    def read(self) -> None: ...
    def image_count(self): ...
    def integerdepth(self): ...
    def dataoffset(self): ...
