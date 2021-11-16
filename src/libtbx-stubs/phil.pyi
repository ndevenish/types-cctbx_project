from io import StringIO
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, Type, Union

from iotbx.phil import (
    atom_selection_converters,
    space_group_converters,
    unit_cell_converters,
)
from libtbx.phil.tokenizer import word
from scitbx_array_family_flex_ext import int

def alias_path(self: Union[scope, definition]) -> None: ...
def bool_from_words(words: List[word], path: str) -> Optional[bool]: ...
def definition_converters_from_words(
    words: List[word],
    converter_registry: Dict[str, Any],
    converter_cache: Dict[Any, Any],
) -> Any: ...
def extended_converter_registry(
    additional_converters: List[Any], base_registry: None = ...
) -> Dict[str, Any]: ...
def float_from_number(
    number: Union[float, int], words: List[word], path: str
) -> float: ...
def float_from_words(words: List[word], path: str) -> Optional[float]: ...
def full_path(self: definition) -> str: ...
def get_converters_phil_type(converters: Any) -> str: ...
def int_from_number(number: int, words: List[word], path: str) -> int: ...
def int_from_words(words: List[word], path: str) -> Optional[int]: ...
def is_plain_auto(words: List[word]) -> bool: ...
def is_plain_none(words: List[word]) -> bool: ...
def is_reserved_identifier(string: str) -> bool: ...
def is_standard_identifier(string: str) -> bool: ...
def normalize_call_expression(expression: str) -> str: ...
def number_from_value_string(
    value_string: Optional[str], words: List[word], path: str
) -> Optional[Union[float, int]]: ...
def number_from_words(words: List[word], path: str) -> Optional[Union[float, int]]: ...
def numbers_from_words(
    words: List[word], path: str
) -> Optional[Union[List[int], List[Union[int, float]], List[float]]]: ...
def parse(
    input_string: Optional[str] = ...,
    source_info: Optional[str] = ...,
    file_name: None = ...,
    converter_registry: Optional[
        Dict[
            str,
            Union[
                Type[words_converters],
                Type[strings_converters],
                Type[str_converters],
                Type[qstr_converters],
                Type[path_converters],
                Type[key_converters],
                Type[bool_converters],
                Type[int_converters],
                Type[float_converters],
                Type[ints_converters],
                Type[floats_converters],
                Type[choice_converters],
                Type[unit_cell_converters],
                Type[space_group_converters],
                Type[atom_selection_converters],
            ],
        ]
    ] = ...,
    process_includes: bool = ...,
    include_stack: None = ...,
) -> scope: ...
def process_include_scope(
    converter_registry: Dict[str, Any],
    include_stack: List[Any],
    object: definition,
    import_path: str,
    phil_path: None,
) -> scope: ...
def show_attributes(
    self: Union[scope, definition],
    out: StringIO,
    prefix: str,
    attributes_level: int,
    print_width: int,
) -> None: ...
def str_from_words(words: List[word]) -> Optional[str]: ...

class _check_value_base:
    def _check_value(
        self,
        value: Union[float, int],
        path_producer: Callable,
        words: Optional[List[word]] = ...,
    ) -> None: ...

class bool_converters:
    def as_words(
        self, python_object: Optional[bool], master: definition
    ) -> List[tokenizer.word]: ...
    def from_words(self, words: List[word], master: definition) -> Optional[bool]: ...

class choice_converters:
    def __init__(self, multi: bool = ...) -> None: ...
    def as_words(
        self, python_object: None, master: definition
    ) -> List[tokenizer.word]: ...
    def fetch(
        self, source_words: List[word], master: definition, ignore_errors: bool = ...
    ) -> definition: ...
    def from_words(self, words: List[word], master: definition) -> Optional[str]: ...

class definition:
    def __init__(
        self,
        name: str,
        words: List[word],
        primary_id: Optional[int] = ...,
        primary_parent_scope: Optional[scope] = ...,
        is_disabled: bool = ...,
        is_template: int = ...,
        where_str: str = ...,
        merge_names: bool = ...,
        tmp: Optional[bool] = ...,
        help: Optional[str] = ...,
        caption: None = ...,
        short_caption: Optional[str] = ...,
        optional: None = ...,
        type: Optional[Any] = ...,
        multiple: Optional[bool] = ...,
        input_size: None = ...,
        style: None = ...,
        expert_level: Optional[int] = ...,
        deprecated: None = ...,
        alias: None = ...,
    ) -> None: ...
    def _all_definitions(
        self,
        suppress_multiple: bool,
        select_tmp: None,
        parent: scope,
        parent_path: str,
        result: List[Union[object_locator, Any]],
    ) -> None: ...
    def _type_from_words(self) -> Callable: ...
    def alias_path(self) -> None: ...
    def as_str(
        self,
        prefix: str = ...,
        expert_level: None = ...,
        attributes_level: int = ...,
        print_width: None = ...,
    ) -> str: ...
    def assign_attribute(
        self,
        name: str,
        words: List[word],
        converter_registry: Dict[str, Any],
        converter_cache: Dict[Any, Any],
    ) -> None: ...
    def copy(self) -> definition: ...
    def customized_copy(
        self, name: Optional[str] = ..., words: Optional[List[word]] = ...
    ) -> definition: ...
    def extract(self, parent: Optional[scope_extract] = ...) -> Any: ...
    def extract_format(self, source: Optional[definition] = ...) -> definition: ...
    def fetch(
        self,
        source: definition,
        diff: bool = ...,
        skip_incompatible_objects: bool = ...,
    ) -> definition: ...
    def fetch_value(
        self,
        source: definition,
        diff_mode: bool = ...,
        skip_incompatible_objects: bool = ...,
    ) -> definition: ...
    def format(self, python_object: Any) -> definition: ...
    def full_path(self) -> str: ...
    def get_without_substitution(
        self, path: str, alias_path: None = ...
    ) -> List[Union[Any, definition]]: ...
    def has_attribute_with_name(self, name: str) -> bool: ...
    def resolve_variables(self, diff_mode: bool = ...) -> definition: ...
    def show(
        self,
        out: Optional[StringIO] = ...,
        merged_names: List[Any] = ...,
        prefix: str = ...,
        expert_level: None = ...,
        attributes_level: int = ...,
        print_width: Optional[int] = ...,
    ) -> None: ...

class float_converters:
    def _value_as_str(self, value: float) -> str: ...
    def _value_from_words(self, words: List[word], path: str) -> Optional[float]: ...

class floats_converters:
    def _value_as_str(self, value: float) -> str: ...
    def _value_from_number(
        self, number: Union[float, int], words: List[word], path: str
    ) -> float: ...

class int_converters:
    def _value_as_str(self, value: int) -> str: ...
    def _value_from_words(self, words: List[word], path: str) -> Optional[int]: ...

class ints_converters:
    def _value_as_str(self, value: int) -> str: ...
    def _value_from_number(self, number: int, words: List[word], path: str) -> int: ...

class number_converters_base:
    def __init__(
        self,
        value_min: Optional[Union[float, int]] = ...,
        value_max: Optional[float] = ...,
        allow_none: bool = ...,
    ) -> None: ...
    def as_words(
        self, python_object: Optional[Union[float, int]], master: definition
    ) -> List[tokenizer.word]: ...
    def from_words(
        self, words: List[word], master: definition
    ) -> Optional[Union[float, int]]: ...

class numbers_converters_base:
    def __init__(
        self,
        size: Optional[int] = ...,
        size_min: Optional[int] = ...,
        size_max: Optional[int] = ...,
        value_min: Optional[int] = ...,
        value_max: Optional[int] = ...,
        allow_none_elements: bool = ...,
        allow_auto_elements: bool = ...,
    ) -> None: ...
    def _check_size(
        self, size: int, path_producer: Callable, words: Optional[List[word]] = ...
    ) -> None: ...
    def as_words(
        self, python_object: Optional[Union[List[int], List[float]]], master: definition
    ) -> List[tokenizer.word]: ...
    def from_words(
        self, words: List[word], master: definition
    ) -> Optional[Union[List[int], List[float]]]: ...

class object_locator:
    def __init__(self, parent: scope, path: str, object: definition) -> None: ...

class scope:
    def __init__(
        self,
        name: str,
        objects: Optional[
            Union[List[scope], List[Union[scope, definition]], List[definition]]
        ] = ...,
        primary_id: Optional[int] = ...,
        primary_parent_scope: Optional[scope] = ...,
        is_disabled: bool = ...,
        is_template: int = ...,
        where_str: str = ...,
        merge_names: bool = ...,
        style: None = ...,
        help: Optional[str] = ...,
        caption: None = ...,
        short_caption: Optional[str] = ...,
        optional: None = ...,
        call: None = ...,
        multiple: Optional[bool] = ...,
        sequential_format: None = ...,
        disable_add: None = ...,
        disable_delete: None = ...,
        expert_level: Optional[int] = ...,
        alias: None = ...,
    ) -> None: ...
    def _all_definitions(
        self,
        suppress_multiple: bool,
        select_tmp: None,
        parent: scope,
        parent_path: str,
        result: List[Union[object_locator, Any]],
    ) -> None: ...
    def active_objects(self) -> Iterator[Union[definition, scope]]: ...
    def adopt(self, object: Union[scope, definition]) -> None: ...
    def alias_path(self) -> None: ...
    def all_definitions(
        self, suppress_multiple: bool = ..., select_tmp: None = ...
    ) -> List[object_locator]: ...
    def as_str(
        self,
        prefix: str = ...,
        expert_level: None = ...,
        attributes_level: int = ...,
        print_width: None = ...,
    ) -> str: ...
    def assign_attribute(
        self,
        name: str,
        words: List[word],
        scope_extract_call_proxy_cache: Dict[Any, Any],
    ) -> None: ...
    def change_primary_parent_scope(self, new_value: scope) -> scope: ...
    def copy(self) -> scope: ...
    def customized_copy(
        self,
        name: None = ...,
        objects: Optional[List[Union[scope, definition, Any]]] = ...,
    ) -> scope: ...
    def extract(self, parent: Optional[scope_extract] = ...) -> scope_extract: ...
    def extract_format(self, source: Optional[scope] = ...) -> scope: ...
    def fetch(
        self,
        source: Optional[scope] = ...,
        sources: Optional[List[scope]] = ...,
        track_unused_definitions: bool = ...,
        diff: bool = ...,
        skip_incompatible_objects: bool = ...,
    ) -> scope: ...
    def format(self, python_object: scope_extract) -> scope: ...
    def get(
        self, path: str, with_substitution: bool = ..., alias_path: None = ...
    ) -> scope: ...
    def get_without_substitution(
        self, path: str, alias_path: None = ...
    ) -> List[Union[scope, definition, Any]]: ...
    def has_attribute_with_name(self, name: str) -> bool: ...
    def master_active_objects(self) -> Iterator[Union[definition, scope]]: ...
    def process_includes(
        self,
        converter_registry: Dict[str, Any],
        reference_directory: None,
        include_stack: None = ...,
    ) -> scope: ...
    def resolve_variables(self) -> scope: ...
    def show(
        self,
        out: Optional[StringIO] = ...,
        merged_names: List[Any] = ...,
        prefix: str = ...,
        expert_level: None = ...,
        attributes_level: int = ...,
        print_width: Optional[int] = ...,
    ) -> None: ...

class scope_extract:
    def __init__(
        self, name: str, parent: Optional[scope_extract], call: None
    ) -> None: ...
    def __phil_get__(self, name: str) -> Any: ...
    def __phil_join__(self, other: scope_extract) -> None: ...
    def __phil_set__(
        self, name: str, optional: None, multiple: Optional[bool], value: Any
    ) -> None: ...
    def __setattr__(
        self,
        name: str,
        value: Union[
            Tuple[int, int, int],
            Tuple[float, float, float],
            List[float],
            int,
            List[int],
        ],
    ) -> None: ...

class scope_extract_list:
    def __init__(self, optional: None) -> None: ...

class str_converters:
    def as_words(
        self, python_object: Optional[str], master: definition
    ) -> List[tokenizer.word]: ...
    def from_words(self, words: List[word], master: definition) -> Optional[str]: ...

class variable_substitution_fragment:
    def __init__(self, is_variable: bool, value: str) -> None: ...

class variable_substitution_proxy:
    def __init__(self, word: word) -> None: ...
    def get_new_words(self) -> List[word]: ...
