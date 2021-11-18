from typing import Any, List, Literal, Optional, Union

from cctbx import uctbx
from libtbx import AutoType
from libtbx.phil import definition, qstr_converters, scope
from libtbx.phil.tokenizer import word

def parse(
    input_string: Optional[str] = ...,
    source_info: Optional[Any] = ...,
    file_name: Optional[Any] = ...,
    converter_registry: Optional[Any] = ...,
    process_includes: bool = ...,
) -> scope: ...

class unit_cell_converters:
    phil_type: str
    def as_words(
        self, python_object: Union[AutoType, uctbx.unit_cell, None], master: definition
    ) -> List[word]: ...
    def from_words(self, words: List[word], master: definition) -> uctbx.unit_cell: ...

class space_group_converters:
    phil_type: str
    def from_words(self, words, master): ...
    def as_words(self, python_object, master): ...

class atom_selection_converters(qstr_converters):
    phil_type: str
    def from_words(self, words, master): ...

default_converter_registry: Any

def read_default(
    caller_file_name,
    params_extension: str = ...,
    converter_registry: Optional[Any] = ...,
    process_includes: bool = ...,
): ...
def process_command_line(args, master_string, parse: Optional[Any] = ...): ...

class process_command_line_with_files:
    master: Any
    pdb_file_def: Any
    reflection_file_def: Any
    cif_file_def: Any
    cif_objects: Any
    map_file_def: Any
    seq_file_def: Any
    pickle_file_def: Any
    ncs_file_def: Any
    directory_def: Any
    integer_def: Any
    float_def: Any
    space_group_def: Any
    unit_cell_def: Any
    unused_args: Any
    work: Any
    def __init__(
        self,
        args,
        master_phil: Optional[Any] = ...,
        master_phil_string: Optional[Any] = ...,
        pdb_file_def: Optional[Any] = ...,
        reflection_file_def: Optional[Any] = ...,
        map_file_def: Optional[Any] = ...,
        cif_file_def: Optional[Any] = ...,
        seq_file_def: Optional[Any] = ...,
        pickle_file_def: Optional[Any] = ...,
        ncs_file_def: Optional[Any] = ...,
        directory_def: Optional[Any] = ...,
        integer_def: Optional[Any] = ...,
        float_def: Optional[Any] = ...,
        space_group_def: Optional[Any] = ...,
        unit_cell_def: Optional[Any] = ...,
        usage_string: Optional[Any] = ...,
    ) -> None: ...
    def get_file_type_count(self, file_type): ...
    def __call__(self, arg): ...
    def process_other(self, arg): ...
    def get_cached_file(self, file_name): ...
    def get_file(self, file_name, force_type: Optional[Any] = ...): ...

class setup_app_generic:
    master_phil: Any
    def __init__(self, master_phil_path) -> None: ...
    def __call__(self, args): ...
    def parse_command_line_phil_args(
        self,
        args,
        master_phil,
        command_name,
        usage_opts,
        app_options,
        home_scope,
        log=...,
    ): ...
    def load_from_cache_if_possible(self, phil_path): ...
