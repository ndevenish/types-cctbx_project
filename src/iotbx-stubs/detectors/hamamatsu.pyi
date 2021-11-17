from iotbx.detectors.adsc import ADSCImage as ADSCImage

class HamamatsuImage(ADSCImage):
    vendortype: str
    def __init__(self, filename) -> None: ...
    def readHeader(self) -> None: ...  # type: ignore # mismatches parent
