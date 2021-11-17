from typing import (
    Any,
    Container,
    Iterator,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
)

T = TypeVar("T")

def flex_proxy(): ...
def numpy_proxy(): ...

class rec:
    container_type: Type[Sequence]
    elems: Sequence
    n: Tuple[int]
    def __init__(self, elems: Container, n: Sequence[int]) -> None: ...
    def n_rows(self) -> int: ...
    def n_columns(self) -> int: ...
    def __neg__(self) -> rec: ...
    def __add__(self, other) -> rec: ...
    def __sub__(self, other) -> rec: ...
    def __mul__(self, other: Union[rec, Sequence, float]) -> rec: ...
    def __rmul__(self, other: Union[rec, Sequence, float]) -> rec: ...
    def __div__(self, other: float) -> rec: ...
    def __truediv__(self, other: float) -> rec: ...
    def __floordiv__(self, other: float) -> rec: ...
    def __mod__(self, other: float) -> rec: ...
    def transpose_multiply(self, other: Optional[Any] = ...): ...
    def __call__(self, ir, ic): ...
    def __len__(self): ...
    def __getitem__(self, i): ...
    def as_float(self): ...
    def as_boost_rational(self): ...
    def as_int(self, rounding: bool = ...): ...
    def as_numpy_array(self): ...
    def each_abs(self): ...
    def each_mod_short(self, period: int = ...): ...
    def min(self): ...
    def max(self): ...
    def min_index(self): ...
    def max_index(self): ...
    def sum(self): ...
    def product(self): ...
    def trace(self): ...
    def norm_sq(self): ...
    def round(self, digits): ...
    def __abs__(self): ...
    length_sq: Any
    length: Any
    def normalize(self): ...
    def dot(self, other: Optional[Any] = ...): ...
    def cross(self, other): ...
    def is_r3_rotation_matrix_rms(self): ...
    def is_r3_rotation_matrix(self, rms_tolerance: float = ...): ...
    def is_r3_identity_matrix(self): ...
    def is_col_zero(self): ...
    def is_zero(self): ...
    def is_approx_zero(self, eps): ...
    def unit_quaternion_as_r3_rotation_matrix(self): ...
    def r3_rotation_matrix_as_x_y_z_angles(
        self, deg: bool = ..., alternate_solution: bool = ...
    ): ...
    def r3_rotation_matrix_as_unit_quaternion(self): ...
    def unit_quaternion_product(self, other): ...
    def quaternion_inverse(self): ...
    def unit_quaternion_as_axis_and_angle(self, deg: bool = ...): ...
    def axis_and_angle_as_unit_quaternion(self, angle, deg: bool = ...): ...
    def axis_and_angle_as_r3_rotation_matrix(self, angle, deg: bool = ...): ...
    def axis_and_angle_as_r3_derivative_wrt_angle(
        self, angle, deg: bool = ..., second_order: bool = ...
    ): ...
    def rt_for_rotation_around_axis_through(self, point, angle, deg: bool = ...): ...
    def ortho(self): ...
    def rotate_around_origin(self, axis, angle, deg: bool = ...): ...
    def rotate_2d(self, angle, deg: bool = ...): ...
    def rotate(self, axis, angle, deg: bool = ...): ...
    def vector_to_001_rotation(
        self,
        sin_angle_is_zero_threshold: float = ...,
        is_normal_vector_threshold: float = ...,
    ): ...
    def outer_product(self, other: Optional[Any] = ...): ...
    def cos_angle(self, other, value_if_undefined: Optional[Any] = ...): ...
    def angle(
        self, other, value_if_undefined: Optional[Any] = ..., deg: bool = ...
    ): ...
    def rotation_angle(self, eps: float = ...): ...
    def accute_angle(
        self, other, value_if_undefined: Optional[Any] = ..., deg: bool = ...
    ): ...
    def is_square(self): ...
    def determinant(self): ...
    def co_factor_matrix_transposed(self): ...
    def inverse(self): ...
    def transpose(self): ...
    def mathematica_form(
        self,
        label: str = ...,
        one_row_per_line: bool = ...,
        format: Optional[Any] = ...,
        prefix: str = ...,
        matrix_form: bool = ...,
    ): ...
    def matlab_form(
        self,
        label: str = ...,
        one_row_per_line: bool = ...,
        format: Optional[Any] = ...,
        prefix: str = ...,
    ): ...
    def as_list_of_lists(self): ...
    def as_sym_mat3(self): ...
    def as_mat3(self): ...
    def as_flex_double_matrix(self): ...
    def as_flex_int_matrix(self): ...
    def extract_block(self, stop, start=..., step=...): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def resolve_partitions(self): ...
    # Lie: This is not declared on the real class, but we need to notify mypy that it is iterable
    def __iter__(self) -> Iterator: ...

class mutable_rec(rec):
    container_type: Any
    def __setitem__(self, i, x) -> None: ...

class row_mixin:
    def __init__(self, elems) -> None: ...

class row(row_mixin, rec): ...
class mutable_row(row_mixin, mutable_rec): ...

class col_mixin:
    def __init__(self, elems) -> None: ...
    @classmethod
    def random(cls: T, n: int, a: float, b: float) -> T: ...

class col(col_mixin, rec): ...
class mutable_col(col_mixin, mutable_rec): ...

class sqr(rec):
    def __init__(self, elems) -> None: ...

class diag(rec):
    def __init__(self, diag_elems) -> None: ...

class identity(diag):
    def __init__(self, n) -> None: ...

class inversion(diag):
    def __init__(self, n) -> None: ...

class sym(rec):
    def __init__(
        self, elems: Optional[Any] = ..., sym_mat3: Optional[Any] = ...
    ) -> None: ...

def zeros(n, mutable: bool = ...): ...
def mutable_zeros(n): ...
def sum(iterable): ...
def cross_product_matrix(vvv): ...
def linearly_dependent_pair_scaling_factor(vector_1, vector_2): ...
def dihedral_angle(sites, deg: bool = ...): ...
def plane_equation(point_1, point_2, point_3): ...
def distance_from_plane(xyz, points): ...
def all_in_plane(points, tolerance): ...
def project_point_on_axis(axis_point_1, axis_point_2, point): ...
def rotate_point_around_axis(
    axis_point_1, axis_point_2, point, angle, deg: bool = ...
): ...

class rt:
    r: Any
    t: Any
    def __init__(self, tuple_r_t) -> None: ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def inverse(self): ...
    def inverse_assuming_orthogonal_r(self): ...
    def as_float(self): ...
    def as_augmented_matrix(self): ...

def col_list(seq): ...
def row_list(seq): ...
def lu_decomposition_in_place(a, n, raise_if_singular: bool = ...): ...
def lu_back_substitution(a, n, pivot_indices, b, raise_if_singular: bool = ...): ...
def inverse_via_lu(m): ...
def determinant_via_lu(m): ...
def find_nearest_orthonormal_matrix(Mmx): ...
def exercise_1(): ...
def exercise_2() -> None: ...
