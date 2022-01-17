from io import StringIO
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Protocol,
    TextIO,
    Tuple,
    Type,
    Union,
    type_check_only,
)

from libtbx import slots_getstate_setstate

from .tokenizer import word

@type_check_only
class PhilConverter(Protocol):
    phil_type: str

default_converter_registry: Dict[str, PhilConverter]

def alias_path(self: Union[scope, definition]) -> Optional[str]: ...
def bool_from_words(words: List[word], path: str) -> Optional[bool]: ...
def definition_converters_from_words(
    words: List[word],
    converter_registry: Dict[str, Any],
    converter_cache: Dict[Any, Any],
) -> Any: ...
def extended_converter_registry(
    additional_converters: List[PhilConverter],
    base_registry: Optional[Dict[str, PhilConverter]] = ...,
) -> Dict[str, PhilConverter]: ...
def get_converters_phil_type(converters: PhilConverter) -> str: ...
def float_from_number(
    number: Union[float, int], words: List[word], path: str
) -> float: ...
def float_from_words(words: List[word], path: str) -> Optional[float]: ...
def full_path(self: Union[scope, definition]) -> str: ...
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
    converter_registry: Optional[Dict[str, Type]] = ...,
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
    ) -> List[word]: ...
    def from_words(self, words: List[word], master: definition) -> Optional[bool]: ...

class choice_converters:
    def __init__(self, multi: bool = ...) -> None: ...
    def as_words(self, python_object: None, master: definition) -> List[word]: ...
    def fetch(
        self, source_words: List[word], master: definition, ignore_errors: bool = ...
    ) -> definition: ...
    def from_words(self, words: List[word], master: definition) -> Optional[str]: ...

class definition(slots_getstate_setstate):
    is_definition: bool
    is_scope: bool
    attribute_names: List[str]
    name: str
    words: List[word]

    primary_id: Optional[int]
    primary_parent_scope: Optional[scope]
    is_disabled: bool
    is_template: int
    where_str: str
    merge_names: bool
    tmp: Any
    help: Optional[str]
    caption: Optional[str]
    short_caption: Optional[str]
    optional: Any
    type: Any
    multiple: Optional[bool]
    input_size: Optional[Any]
    style: Optional[Any]
    expert_level: Optional[int]
    deprecated: Optional[bool]
    alias: Optional[str]
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
        tmp: Optional[Any] = ...,
        help: Optional[str] = ...,
        caption: Optional[str] = ...,
        short_caption: Optional[str] = ...,
        optional: Optional[Any] = ...,
        type: Optional[Any] = ...,
        multiple: Optional[bool] = ...,
        input_size: Optional[Any] = ...,
        style: Optional[Any] = ...,
        expert_level: Optional[int] = ...,
        deprecated: Optional[bool] = ...,
        alias: Optional[str] = ...,
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
    def alias_path(self) -> Optional[str]: ...
    def as_str(
        self,
        prefix: str = ...,
        expert_level: Optional[int] = ...,
        attributes_level: int = ...,
        print_width: Optional[int] = ...,
    ) -> str: ...
    def assign_attribute(
        self,
        name: str,
        words: List[word],
        converter_registry: Dict[str, Any],
        converter_cache: Dict[Any, Any],
    ) -> None: ...
    def assign_tmp(self, value: Any, active_only: bool = ...) -> None: ...
    def copy(self) -> definition: ...
    def customized_copy(
        self, name: Optional[str] = ..., words: Optional[List[word]] = ...
    ) -> definition: ...
    def extract_format(
        self, source: Optional[Union[scope, definition]] = ...
    ) -> definition: ...
    def extract(self, parent: Optional[scope_extract] = ...) -> Any: ...
    def fetch_diff(self, source, skip_incompatible_objects: bool = ...): ...
    def fetch_value(
        self,
        source: definition,
        diff_mode: bool = ...,
        skip_incompatible_objects: bool = ...,
    ) -> definition: ...
    def fetch(
        self,
        source: definition,
        diff: bool = ...,
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
        out: Optional[TextIO] = ...,
        merged_names: List[Any] = ...,
        prefix: str = ...,
        expert_level: Optional[int] = ...,
        attributes_level: int = ...,
        print_width: Optional[int] = ...,
    ) -> None: ...
    def try_extract_format(self): ...
    def try_extract(self): ...
    def try_tokenize(self, input_string, source_info: Optional[Any] = ...): ...
    def unique(self): ...
    def validate_and_format(self, input_string, source_info: Optional[Any] = ...): ...
    def validate(self, input_string, source_info: Optional[Any] = ...): ...

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
    value_min: Any
    value_max: Any
    allow_none: Any
    def __init__(
        self,
        value_min: Optional[Union[float, int]] = ...,
        value_max: Optional[float] = ...,
        allow_none: bool = ...,
    ) -> None: ...
    def as_words(
        self, python_object: Optional[Union[float, int]], master: definition
    ) -> List[word]: ...
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
    ) -> List[word]: ...
    def from_words(
        self, words: List[word], master: definition
    ) -> Optional[Union[List[int], List[float]]]: ...

class object_locator:
    def __init__(self, parent: scope, path: str, object: definition) -> None: ...

class scope:
    is_definition: bool
    is_scope: bool
    deprecated: bool
    attribute_names: Any
    name: Any
    objects: Any
    primary_id: Any
    primary_parent_scope: Any
    is_disabled: Any
    is_template: Any
    where_str: Any
    merge_names: Any
    style: Any
    help: Any
    caption: Any
    short_caption: Any
    optional: Any
    call: Any
    multiple: Any
    sequential_format: Any
    disable_add: Any
    disable_delete: Any
    expert_level: Any
    alias: Any
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
        style: Any = ...,
        help: Optional[str] = ...,
        caption: Any = ...,
        short_caption: Optional[str] = ...,
        optional: Any = ...,
        call: Any = ...,
        multiple: Optional[bool] = ...,
        sequential_format: Any = ...,
        disable_add: Any = ...,
        disable_delete: Any = ...,
        expert_level: Optional[int] = ...,
        alias: Any = ...,
    ) -> None: ...
    def _all_definitions(
        self,
        suppress_multiple: bool,
        select_tmp: Any,
        parent: scope,
        parent_path: str,
        result: List[Union[object_locator, Any]],
    ) -> None: ...
    def active_objects(self) -> Iterator[Union[definition, scope]]: ...
    def adopt(self, object: Union[scope, definition]) -> None: ...
    def alias_path(self) -> Optional[str]: ...
    def all_definitions(
        self, suppress_multiple: bool = ..., select_tmp: Any = ...
    ) -> List[object_locator]: ...
    def as_str(
        self,
        prefix: str = ...,
        expert_level: Any = ...,
        attributes_level: int = ...,
        print_width: Any = ...,
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
        name: Any = ...,
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
        self, path: str, with_substitution: bool = ..., alias_path: Any = ...
    ) -> scope: ...
    def get_without_substitution(
        self, path: str, alias_path: Any = ...
    ) -> List[Union[scope, definition, Any]]: ...
    def has_attribute_with_name(self, name: str) -> bool: ...
    def master_active_objects(self) -> Iterator[Union[definition, scope]]: ...
    def process_includes(
        self,
        converter_registry: Dict[str, Any],
        reference_directory: Any,
        include_stack: Any = ...,
    ) -> scope: ...
    def resolve_variables(self) -> scope: ...
    def show(
        self,
        out: Optional[TextIO] = ...,
        merged_names: List[Any] = ...,
        prefix: str = ...,
        expert_level: Any = ...,
        attributes_level: int = ...,
        print_width: Optional[int] = ...,
    ) -> None: ...
    def is_empty(self): ...
    def full_path(self): ...
    def assign_tmp(self, value, active_only: bool = ...) -> None: ...
    def adopt_scope(self, other) -> None: ...
    def lexical_get(self, path, stop_id, search_up: bool = ...): ...
    def clone(self, python_object, converter_registry: Optional[Any] = ...): ...
    def fetch_diff(
        self,
        source: Optional[Any] = ...,
        sources: Optional[Any] = ...,
        track_unused_definitions: bool = ...,
        skip_incompatible_objects: bool = ...,
    ): ...
    def unique(self): ...
    def command_line_argument_interpreter(
        self, home_scope: Optional[Any] = ..., argument_description: Optional[Any] = ...
    ): ...

class scope_extract:
    def __init__(
        self, name: str, parent: Optional[scope_extract], call: None
    ) -> None: ...
    def __inject__(self, name, value) -> None: ...
    def __phil_get__(self, name: str) -> Any: ...
    def __phil_join__(self, other: scope_extract) -> None: ...
    def __phil_path__(self, object_name: Optional[Any] = ...): ...
    def __phil_path_and_value__(self, object_name): ...
    def __setattr__(self, name, value) -> None: ...
    def __phil_set__(
        self, name: str, optional: bool, multiple: Optional[bool], value: Any
    ) -> None: ...
    def __call__(self, **keyword_args): ...

class scope_extract_list:
    __phil_optional__: Any
    def __init__(self, optional: None) -> None: ...

class str_converters:
    def as_words(
        self, python_object: Optional[str], master: definition
    ) -> List[word]: ...
    def from_words(self, words: List[word], master: definition) -> Optional[str]: ...

class variable_substitution_fragment:
    def __init__(self, is_variable: bool, value: str) -> None: ...

class variable_substitution_proxy:
    def __init__(self, word: word) -> None: ...
    def get_new_words(self) -> List[word]: ...

class PhilDeprecationWarning(DeprecationWarning): ...

def tokenize_value_literal(input_string, source_info): ...

class words_converters:
    phil_type: str
    def from_words(self, words, master): ...
    def as_words(self, python_object, master): ...

def strings_as_words(python_object): ...

class qstr_converters:
    phil_type: str
    def from_words(self, words, master): ...
    def as_words(self, python_object, master): ...

class path_converters(str_converters):
    phil_type: str
    def from_words(self, words, master): ...

class key_converters(str_converters):
    phil_type: str

def extract_args(*args, **keyword_args): ...

class try_tokenize_proxy:
    error_message: Any
    tokenized: Any
    def __init__(self, error_message, tokenized) -> None: ...

class try_extract_proxy:
    error_message: Any
    extracted: Any
    def __init__(self, error_message, extracted) -> None: ...

class try_format_proxy:
    error_message: Any
    formatted: Any
    def __init__(self, error_message, formatted) -> None: ...

class scope_extract_call_proxy_object:
    where_str: Any
    expression: Any
    callable: Any
    keyword_args: Any
    def __init__(self, where_str, expression, callable, keyword_args) -> None: ...

def scope_extract_call_proxy(full_path, words, cache): ...

class scope_extract_attribute_error: ...
class scope_extract_is_disabled: ...

def read_default(
    caller_file_name,
    params_extension: str = ...,
    converter_registry: Optional[Any] = ...,
    process_includes: bool = ...,
): ...
def process_command_line(args, master_string, parse: Optional[Any] = ...): ...
def find_scope(current_phil, scope_name): ...
def change_default_phil_values(
    master_phil_str,
    new_default_phil_str,
    phil_parse: Optional[Any] = ...,
    expert_level: int = ...,
    attributes_level: int = ...,
): ...
