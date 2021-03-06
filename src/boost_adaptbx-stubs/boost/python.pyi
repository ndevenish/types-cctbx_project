from __future__ import annotations

from types import ModuleType
from typing import Any, Callable, Type, Union

from .boost_python_meta_ext import *

platform_info: str

def import_ext(name: str, optional: bool = ...) -> ModuleType:
    """
    Import a python 'Extension' module with special tbx-related flags.

    If on linux, the shared library will be imported into global process
    namespace with both os.RTLD_GLOBAL and os.RTLD_NOW via
    sys.setdlopenflags. The flags will be restored after loading.

    In all platforms, if importing fails, it will attempt to demangle
    the C++ symbol before re-raising the ImportError.
    """

class trapping:
    def __init__(
        self, division_by_zero: bool = ..., invalid: bool = ..., overflow: bool = ...
    ) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

def c_sizeof(typename: str) -> int: ...

class floating_point_exceptions_type:
    def __init__(self) -> None: ...
    @property
    def division_by_zero_trapped(self) -> bool: ...
    @property.setter
    def division_by_zero_trapped(self, state: bool) -> None: ...
    @property
    def invalid_trapped(self) -> bool: ...
    @property.setter
    def invalid_trapped(self, state: bool) -> None: ...
    @property
    def overflow_trapped(self) -> bool: ...
    @property.setter
    def overflow_trapped(self, state: bool) -> None: ...

floating_point_exceptions: floating_point_exceptions_type

class gcc_version:
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...

def inject(target_class: type, *mixin_classes: type) -> None: ...
def inject_into(
    target_class: type | Any, *mixin_classes: type
) -> Callable[[type], None]: ...
def process_docstring_options(env_var: str = ...) -> Any: ...

docstring_options: Any
