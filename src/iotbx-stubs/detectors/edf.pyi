from typing import Any, Optional

def file_object_from_file_name(filename): ...

class EDFImage:
    obj: Any
    headersize: int
    data_dimension: Any
    parameters: Any
    header: Any
    linearintdata: Any
    type_size: Any
    def __init__(self, filename) -> None: ...
    def readHeader(self, external_keys: Optional[Any] = ...) -> None: ...
    def read(self) -> None: ...
