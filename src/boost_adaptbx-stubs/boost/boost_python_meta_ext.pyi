from __future__ import annotations

from typing import IO

class streambuf:
    def __init__(self, python_file_obj: IO, buffer_size: int) -> None: ...
    @property
    def default_buffer_size(self) -> int: ...
    @property.setter
    def default_buffer_size(self, int) -> None: ...
