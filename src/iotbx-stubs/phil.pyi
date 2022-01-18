from __future__ import annotations

from typing import Any, List, Literal, Optional, Union

from cctbx import uctbx
from libtbx import AutoType
from libtbx.phil import definition, qstr_converters, scope
from libtbx.phil.tokenizer import word

def parse(
    input_string: str | None = ...,
    source_info: Any | None = ...,
    file_name: Any | None = ...,
    converter_registry: Any | None = ...,
    process_includes: bool = ...,
) -> scope: ...

class unit_cell_converters:
    phil_type: str
    def as_words(
        self, python_object: AutoType | uctbx.unit_cell | None, master: definition
    ) -> list[word]: ...
    def from_words(self, words: list[word], master: definition) -> uctbx.unit_cell: ...

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
    converter_registry: Any | None = ...,
    process_includes: bool = ...,
): ...
def process_command_line(args, master_string, parse: Any | None = ...): ...

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
        master_phil: Any | None = ...,
        master_phil_string: Any | None = ...,
        pdb_file_def: Any | None = ...,
        reflection_file_def: Any | None = ...,
        map_file_def: Any | None = ...,
        cif_file_def: Any | None = ...,
        seq_file_def: Any | None = ...,
        pickle_file_def: Any | None = ...,
        ncs_file_def: Any | None = ...,
        directory_def: Any | None = ...,
        integer_def: Any | None = ...,
        float_def: Any | None = ...,
        space_group_def: Any | None = ...,
        unit_cell_def: Any | None = ...,
        usage_string: Any | None = ...,
    ) -> None: ...
    def get_file_type_count(self, file_type): ...
    def __call__(self, arg): ...
    def process_other(self, arg): ...
    def get_cached_file(self, file_name): ...
    def get_file(self, file_name, force_type: Any | None = ...): ...

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
