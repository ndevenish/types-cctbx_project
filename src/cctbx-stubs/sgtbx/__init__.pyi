# Basic autogenerated subs. Very incomplete.

from __future__ import annotations

from typing import Any, ClassVar, Optional

cb_r_den: int
cb_t_den: int
sg_t_den: int

class space_group_info:
    def __init__(
        self,
        symbol: str | None = ...,
        table_id: Any | None = ...,
        group: space_group | None = ...,
        number: int | None = ...,
        space_group_t_den: Any | None = ...,
    ) -> None: ...
    def change_of_basis_op_to_primitive_setting(self) -> change_of_basis_op: ...
    def change_of_basis_op_to_reference_setting(self) -> change_of_basis_op: ...
    def group(self) -> space_group: ...
    def type(
        self, tidy_cb_op: bool = ..., r_den: Any = ..., t_den: Any = ...
    ) -> space_group_type: ...
    def any_generator_set(self): ...
    def reciprocal_space_asu(self): ...
    def direct_space_asu(self): ...
    def brick(self): ...
    def wyckoff_table(self): ...
    def structure_seminvariants(self): ...
    def reference_setting(self): ...
    def is_reference_setting(self): ...
    def as_reference_setting(self): ...
    def change_basis(self, cb_op): ...
    def change_of_basis_op_to_other_hand(self): ...
    def change_hand(self): ...
    def primitive_setting(self): ...
    def change_of_basis_op_to(self, other): ...
    def reflection_intensity_equivalent_groups(self, anomalous_flag: bool = ...): ...
    def symbol_and_number(self): ...
    def show_summary(self, f: Any | None = ..., prefix: str = ...) -> None: ...
    def number_of_continuous_allowed_origin_shifts(self): ...
    def subtract_continuous_allowed_origin_shifts(self, translation_frac): ...
    def is_allowed_origin_shift(self, shift, tolerance): ...
    def any_compatible_unit_cell(
        self, volume: Any | None = ..., asu_volume: Any | None = ...
    ): ...
    def any_compatible_crystal_symmetry(
        self, volume: Any | None = ..., asu_volume: Any | None = ...
    ): ...
    def cif_symmetry_code(self, rt_mx, full_code: bool = ..., sep: str = ...): ...

class any_generator_set:
    def __init__(self, space_group, z2c_r_den=..., z2c_t_den=...) -> None: ...
    # These came in stub generator but apparently not visible in uninitiated runtime?
    # def p_gen(self) -> Any: ...
    # def set_primitive(self) -> Any: ...
    # def z_gen(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class brick:
    def __init__(self, *args, **kwargs) -> None: ...
    def as_string(self) -> Any: ...
    def is_inside(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

class change_of_basis_op:
    __safe_for_unpickling__: ClassVar[bool] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def apply(self, *args, **kwargs) -> Any: ...
    def apply_results_in_non_integral_indices(self, *args, **kwargs) -> Any: ...
    def as_abc(self) -> Any: ...
    def as_hkl(self) -> Any: ...
    def as_xyz(self) -> Any: ...
    def c(self) -> Any: ...
    def c_inv(self) -> Any: ...
    def identity_op(self) -> Any: ...
    def inverse(self) -> Any: ...
    def is_identity_op(self) -> Any: ...
    def is_valid(self) -> Any: ...
    def mod_positive_in_place(self) -> Any: ...
    def mod_short(self) -> Any: ...
    def mod_short_in_place(self) -> Any: ...
    def new_denominators(self, *args, **kwargs) -> Any: ...
    def select(self, bool) -> Any: ...
    def symbol(self) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __call__(self, *args, **kwargs) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class find_affine:
    def __init__(self, *args, **kwargs) -> None: ...
    def cb_mx(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class min_sym_equiv_distance_info:
    def __init__(self, *args, **kwargs) -> None: ...
    def apply(self, *args, **kwargs) -> Any: ...
    def continuous_shifts(self) -> Any: ...
    def diff(self) -> Any: ...
    def dist(self) -> Any: ...
    def i_other(self) -> Any: ...
    def sym_op(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class parse_string:
    def __init__(self, *args, **kwargs) -> None: ...
    def string(self) -> Any: ...
    def where(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class phase_info:
    def __init__(self, *args, **kwargs) -> None: ...
    def ht(self) -> Any: ...
    def ht_angle(self) -> Any: ...
    def is_centric(self) -> Any: ...
    def is_sys_absent(self) -> Any: ...
    def is_valid_phase(self, *args, **kwargs) -> Any: ...
    def nearest_valid_phase(self, *args, **kwargs) -> Any: ...
    def sys_abs_was_tested(self) -> Any: ...
    def t_den(self) -> Any: ...
    def valid_structure_factor(self, std) -> Any: ...
    def __reduce__(self) -> Any: ...

class rank_2_tensor_constraints:
    def __init__(self, *args, **kwargs) -> None: ...
    def all_params(self, *args, **kwargs) -> Any: ...
    def cleanup(self, *args, **kwargs) -> Any: ...
    def gradient_sum_matrix(self, scitbx) -> Any: ...
    def independent_curvatures(self, *args, **kwargs) -> Any: ...
    def independent_gradients(self, *args, **kwargs) -> Any: ...
    def independent_params(self, *args, **kwargs) -> Any: ...
    def indices(self, *args, **kwargs) -> Any: ...
    def initialise(self, *args, **kwargs) -> Any: ...
    def n_dependent_params(self, scitbx) -> Any: ...
    def n_independent_params(self, scitbx) -> Any: ...
    def row_echelon_form(self, scitbx) -> Any: ...
    def __reduce__(self) -> Any: ...
    @property
    def independent_indices(self) -> Any: ...

class rank_3_tensor_constraints:
    def __init__(self, *args, **kwargs) -> None: ...
    def all_params(self, *args, **kwargs) -> Any: ...
    def cleanup(self, *args, **kwargs) -> Any: ...
    def gradient_sum_matrix(self, scitbx) -> Any: ...
    def independent_curvatures(self, *args, **kwargs) -> Any: ...
    def independent_gradients(self, *args, **kwargs) -> Any: ...
    def independent_params(self, *args, **kwargs) -> Any: ...
    def indices(self, *args, **kwargs) -> Any: ...
    def initialise(self, *args, **kwargs) -> Any: ...
    def n_dependent_params(self, scitbx) -> Any: ...
    def n_independent_params(self, scitbx) -> Any: ...
    def row_echelon_form(self, scitbx) -> Any: ...
    def __reduce__(self) -> Any: ...
    @property
    def independent_indices(self) -> Any: ...

class rank_4_tensor_constraints:
    def __init__(self, *args, **kwargs) -> None: ...
    def all_params(self, *args, **kwargs) -> Any: ...
    def cleanup(self, *args, **kwargs) -> Any: ...
    def gradient_sum_matrix(self, scitbx) -> Any: ...
    def independent_curvatures(self, *args, **kwargs) -> Any: ...
    def independent_gradients(self, *args, **kwargs) -> Any: ...
    def independent_params(self, *args, **kwargs) -> Any: ...
    def indices(self, *args, **kwargs) -> Any: ...
    def initialise(self, *args, **kwargs) -> Any: ...
    def n_dependent_params(self, scitbx) -> Any: ...
    def n_independent_params(self, scitbx) -> Any: ...
    def row_echelon_form(self, scitbx) -> Any: ...
    def __reduce__(self) -> Any: ...
    @property
    def independent_indices(self) -> Any: ...

class reciprocal_space_asu:
    def __init__(self, *args, **kwargs) -> None: ...
    def cb_op(self) -> Any: ...
    def is_inside(self, *args, **kwargs) -> Any: ...
    def is_reference(self) -> Any: ...
    def reference_as_string(self) -> Any: ...
    def which(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

class rot_mx:
    def as_rational(self): ...
    def le_page_1982_delta_details(self, reduced_cell, deg: bool = ...): ...
    def le_page_1982_delta(self, reduced_cell, deg: bool = ...): ...
    def lebedev_2005_perturbation(self, reduced_cell): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def accumulate(self) -> Any: ...
    def as_double(self) -> Any: ...
    def as_hkl(self) -> Any: ...
    def as_xyz(self) -> Any: ...
    def cancel(self) -> Any: ...
    def den(self) -> Any: ...
    def determinant(self) -> Any: ...
    def divide(self, int) -> Any: ...
    def info(self) -> Any: ...
    def inverse(self) -> Any: ...
    def inverse_cancel(self) -> Any: ...
    def is_unit_mx(self) -> Any: ...
    def is_valid(self) -> Any: ...
    def minus_unit_mx(self) -> Any: ...
    def multiply(self, *args, **kwargs) -> Any: ...
    def new_denominator(self, int) -> Any: ...
    def num(self) -> Any: ...
    def order(self) -> Any: ...
    def scale(self, int) -> Any: ...
    def transpose(self) -> Any: ...
    def type(self) -> Any: ...
    def __call__(self, scitbx) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __hash__(self) -> Any: ...
    def __mul__(self, scitbx) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __rmul__(self, scitbx) -> Any: ...

class rot_mx_info:
    def basis_of_invariant(self): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def ev(self) -> Any: ...
    def sense(self) -> Any: ...
    def type(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class rt_mx:
    def as_rational(self): ...
    def as_4x4_rational(self): ...
    def show_geometrical_elements(self, out: Any | None = ...) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def add_unit_shifts_minimum_distance(self, *args, **kwargs) -> Any: ...
    def as_double_array(self) -> Any: ...
    def as_int_array(self) -> Any: ...
    def as_xyz(self) -> Any: ...
    def cancel(self) -> Any: ...
    def inverse(self) -> Any: ...
    def inverse_cancel(self) -> Any: ...
    def is_unit_mx(self) -> Any: ...
    def is_valid(self) -> Any: ...
    def mod_positive(self) -> Any: ...
    def mod_short(self) -> Any: ...
    def multiply(self, *args, **kwargs) -> Any: ...
    def new_denominators(self, *args, **kwargs) -> Any: ...
    def r(self) -> Any: ...
    def refine_gridding(self, scitbx) -> Any: ...
    def t(self) -> Any: ...
    def unit_mx(self) -> Any: ...
    def unit_shifts_minimum_distance(self, *args, **kwargs) -> Any: ...
    def __add__(self, scitbx) -> Any: ...
    def __call__(self, scitbx) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mul__(self, scitbx) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class search_symmetry:
    def __init__(self, *args, **kwargs) -> None: ...
    def continuous_shift_flags(self) -> Any: ...
    def continuous_shifts(self) -> Any: ...
    def continuous_shifts_are_principal(self) -> Any: ...
    def flags(self) -> Any: ...
    def projected_subgroup(self) -> Any: ...
    def subgroup(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class search_symmetry_flags:
    def show_summary(self, f: Any | None = ...) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def use_normalizer_k2l(self) -> Any: ...
    def use_normalizer_l2n(self) -> Any: ...
    def use_seminvariants(self) -> Any: ...
    def use_space_group_ltr(self) -> Any: ...
    def use_space_group_symmetry(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class site_constraints:
    def __init__(self, *args, **kwargs) -> None: ...
    def all_params(self, *args, **kwargs) -> Any: ...
    def all_shifts(self, *args, **kwargs) -> Any: ...
    def gradient_sum_matrix(self) -> Any: ...
    def independent_curvatures(self, *args, **kwargs) -> Any: ...
    def independent_gradients(self, scitbx) -> Any: ...
    def independent_params(self, *args, **kwargs) -> Any: ...
    def n_dependent_params(self) -> Any: ...
    def n_independent_params(self) -> Any: ...
    def row_echelon_form(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    @property
    def independent_indices(self) -> Any: ...
    @property
    def row_echelon_constants(self) -> Any: ...
    @property
    def row_echelon_lcm(self) -> Any: ...

class site_symmetry(site_symmetry_ops):
    def __init__(self, *args, **kwargs) -> None: ...
    def check_min_distance_sym_equiv(self) -> Any: ...
    def distance_moved(self) -> Any: ...
    def exact_site(self) -> Any: ...
    def min_distance_sym_equiv(self) -> Any: ...
    def multiplicity(self) -> Any: ...
    def original_site(self) -> Any: ...
    def point_group_type(self) -> Any: ...
    def shortest_distance(self) -> Any: ...
    def space_group(self, *args, **kwargs) -> Any: ...
    def unique_ops(self) -> Any: ...
    def unit_cell(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

class site_symmetry_ops:
    def __getinitargs__(self): ...
    def special_op_simplified(self): ...
    def shelx_fvar_encoding(self, fvars, site, p_tolerance: float = ...): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def adp_constraints(self) -> Any: ...
    def average_u_star(self, scitbx) -> Any: ...
    def cartesian_adp_constraints(self, *args, **kwargs) -> Any: ...
    def change_basis(self, *args, **kwargs) -> Any: ...
    def is_compatible_u_star(self, scitbx) -> Any: ...
    def is_point_group_1(self) -> Any: ...
    def matrices(self) -> Any: ...
    def multiplicity(self) -> Any: ...
    def n_matrices(self) -> Any: ...
    def site_constraints(self) -> Any: ...
    def special_op(self) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class site_symmetry_table:
    def __getinitargs__(self): ...
    def apply_symmetry_sites(self, unit_cell, sites_cart): ...
    def show_special_position_shifts(
        self,
        special_position_settings,
        site_labels,
        sites_frac_original: Any | None = ...,
        sites_cart_original: Any | None = ...,
        sites_frac_exact: Any | None = ...,
        sites_cart_exact: Any | None = ...,
        out: Any | None = ...,
        prefix: str = ...,
    ) -> None: ...
    def discard_symmetry(self): ...
    def symmetry_equivalent_pair_interactions(self, i_seq, j_seq, rt_mx_ji): ...
    def pack_coordinates(self, sites_frac): ...
    def unpack_coordinates(self, packed_coordinates): ...
    def pack_gradients(self, g_frac): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def change_basis(self, *args, **kwargs) -> Any: ...
    def deep_copy(self) -> Any: ...
    def get(self, unsignedlong) -> Any: ...
    def indices(self) -> Any: ...
    def is_special_position(self, unsignedlong) -> Any: ...
    def n_special_positions(self) -> Any: ...
    def n_unique(self) -> Any: ...
    def process(self, *args, **kwargs) -> Any: ...
    def reserve(self, unsignedlong) -> Any: ...
    def select(self, *args, **kwargs) -> Any: ...
    def special_position_indices(self) -> Any: ...
    def table(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class space_group:
    def smx(self, with_inversion: bool = ...) -> None: ...
    def ltr(self) -> None: ...
    def info(self): ...
    def adp_constraints(self): ...
    def cartesian_adp_constraints(self, unit_cell): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def all_ops(self) -> Any: ...
    def average_u_star(self, scitbx) -> Any: ...
    def average_unit_cell(self, *args, **kwargs) -> Any: ...
    def build_derived_acentric_group(self) -> Any: ...
    def build_derived_group(self, *args, **kwargs) -> Any: ...
    def build_derived_laue_group(self) -> Any: ...
    def build_derived_patterson_group(self) -> Any: ...
    def build_derived_point_group(self) -> Any: ...
    def build_derived_reflection_intensity_group(self, bool) -> Any: ...
    def change_basis(self, *args, **kwargs) -> Any: ...
    def change_of_origin_realising_origin_centricity(self) -> Any: ...
    def construct_z2p_op(self) -> Any: ...
    def contains(self, *args, **kwargs) -> Any: ...
    def conventional_centring_type_symbol(self) -> Any: ...
    def crystal_system(self) -> Any: ...
    def epsilon(self, *args, **kwargs) -> Any: ...
    def expand_conventional_centring_type(self, char) -> Any: ...
    def expand_inv(self, *args, **kwargs) -> Any: ...
    def expand_ltr(self, *args, **kwargs) -> Any: ...
    def expand_smx(self, *args, **kwargs) -> Any: ...
    def f_inv(self) -> Any: ...
    def gridding(self) -> Any: ...
    def is_centric(self) -> Any: ...
    def is_chiral(self) -> Any: ...
    def is_compatible_unit_cell(self, *args, **kwargs) -> Any: ...
    def is_origin_centric(self) -> Any: ...
    def is_sys_absent(self, *args, **kwargs) -> Any: ...
    def is_tidy(self) -> Any: ...
    def is_valid_phase(self, *args, **kwargs) -> Any: ...
    def laue_group_type(self) -> Any: ...
    def make_tidy(self) -> Any: ...
    def match_tabulated_settings(self) -> Any: ...
    def multiplicity(self, scitbx) -> Any: ...
    def n_equivalent_positions(self) -> Any: ...
    def n_ltr(self) -> Any: ...
    def n_smx(self) -> Any: ...
    def nearest_valid_phases(self, *args, **kwargs) -> Any: ...
    def order_p(self) -> Any: ...
    def order_z(self) -> Any: ...
    def parse_hall_symbol(self, *args, **kwargs) -> Any: ...
    def phase_restriction(self, *args, **kwargs) -> Any: ...
    def point_group_type(self) -> Any: ...
    def r_den(self) -> Any: ...
    def refine_gridding(self, scitbx) -> Any: ...
    def reset(self) -> Any: ...
    def t_den(self) -> Any: ...
    def type(self) -> Any: ...
    def unique(self, *args, **kwargs) -> Any: ...
    def z2p_op(self) -> Any: ...
    def __call__(self, unsignedlong) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __getitem__(self, unsignedlong) -> Any: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, boost) -> Any: ...

class space_group_symbol_iterator:
    def __init__(self, *args, **kwargs) -> None: ...
    def next(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __iter__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class space_group_symbols:
    def __init__(self, *args, **kwargs) -> None: ...
    def change_of_basis_symbol(self) -> Any: ...
    def crystal_system(self) -> Any: ...
    def extension(self) -> Any: ...
    def hall(self) -> Any: ...
    def hermann_mauguin(self) -> Any: ...
    def laue_group_type(self) -> Any: ...
    def number(self) -> Any: ...
    def point_group_type(self) -> Any: ...
    def qualifier(self) -> Any: ...
    def schoenflies(self) -> Any: ...
    def universal_hermann_mauguin(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class space_group_type:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def addl_generators_of_euclidean_normalizer(self, *args, **kwargs) -> Any: ...
    def cb_op(self) -> Any: ...
    def cb_op_is_tidy(self) -> Any: ...
    def change_of_hand_op(self) -> Any: ...
    def expand_addl_generators_of_euclidean_normalizer(
        self, *args, **kwargs
    ) -> Any: ...
    def group(self) -> Any: ...
    def hall_symbol(self) -> Any: ...
    def is_enantiomorphic(self) -> Any: ...
    def is_symmorphic(self) -> Any: ...
    def lookup_symbol(self) -> Any: ...
    def number(self) -> Any: ...
    def universal_hermann_mauguin_symbol(self) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class ss_vec_mod:
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def m(self) -> Any: ...
    @property
    def v(self) -> Any: ...

class stl_vector_rot_mx:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def extend(self, *args, **kwargs) -> Any: ...
    def insert(self, *args, **kwargs) -> Any: ...
    def size(self, *args, **kwargs) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __len__(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...

class stl_vector_rt_mx:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def extend(self, *args, **kwargs) -> Any: ...
    def insert(self, *args, **kwargs) -> Any: ...
    def size(self, *args, **kwargs) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __len__(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...

class structure_seminvariants:
    def number_of_continuous_allowed_origin_shifts(self): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def apply_mod(self, *args, **kwargs) -> Any: ...
    def continuous_shifts_are_principal(self) -> Any: ...
    def grid_adapted_moduli(self, scitbx) -> Any: ...
    def gridding(self) -> Any: ...
    def is_ss(self, *args, **kwargs) -> Any: ...
    def principal_continuous_shift_flags(self) -> Any: ...
    def refine_gridding(self, scitbx) -> Any: ...
    def select(self, bool) -> Any: ...
    def size(self) -> Any: ...
    def subtract_principal_continuous_shifts(self, *args, **kwargs) -> Any: ...
    def vectors_and_moduli(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class sym_equiv_sites:
    def __init__(self, *args, **kwargs) -> None: ...
    def coordinates(self) -> Any: ...
    def is_special_position(self) -> Any: ...
    def max_accepted_tolerance(self) -> Any: ...
    def original_site(self) -> Any: ...
    def space_group(self, *args, **kwargs) -> Any: ...
    def special_op(self) -> Any: ...
    def sym_op(self, unsignedlong) -> Any: ...
    def sym_op_indices(self) -> Any: ...
    def unit_cell(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

class tensor_rank_2_cartesian_constraints:
    def __init__(self, *args, **kwargs) -> None: ...
    def all_params(self, *args, **kwargs) -> Any: ...
    def independent_gradients(self, scitbx) -> Any: ...
    def independent_params(self, scitbx) -> Any: ...
    def jacobian(self) -> Any: ...
    def n_independent_params(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class tensor_rank_2_constraints:
    def __init__(self, *args, **kwargs) -> None: ...
    def all_params(self, *args, **kwargs) -> Any: ...
    def gradient_sum_matrix(self) -> Any: ...
    def independent_curvatures(self, *args, **kwargs) -> Any: ...
    def independent_gradients(self, scitbx) -> Any: ...
    def independent_params(self, scitbx) -> Any: ...
    def n_dependent_params(self) -> Any: ...
    def n_independent_params(self) -> Any: ...
    def row_echelon_form(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    @property
    def independent_indices(self) -> Any: ...

class tr_vec:
    def as_rational(self): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def as_double(self) -> Any: ...
    def as_string(self) -> Any: ...
    def cancel(self) -> Any: ...
    def den(self) -> Any: ...
    def is_valid(self) -> Any: ...
    def is_zero(self) -> Any: ...
    def minus(self, *args, **kwargs) -> Any: ...
    def mod_positive(self) -> Any: ...
    def mod_short(self) -> Any: ...
    def new_denominator(self, int) -> Any: ...
    def num(self) -> Any: ...
    def plus(self, *args, **kwargs) -> Any: ...
    def scale(self, int) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class translation_part_info:
    def __init__(self, *args, **kwargs) -> None: ...
    def intrinsic_part(self) -> Any: ...
    def location_part(self) -> Any: ...
    def origin_shift(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class wyckoff_mapping:
    def __init__(self, *args, **kwargs) -> None: ...
    def distance_moved(self) -> Any: ...
    def exact_site(self) -> Any: ...
    def original_site(self) -> Any: ...
    def position(self, *args, **kwargs) -> Any: ...
    def representative_site(self) -> Any: ...
    def special_op(self) -> Any: ...
    def sym_op(self) -> Any: ...
    def unit_cell(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

class wyckoff_position:
    def special_op_simplified(self): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def letter(self) -> Any: ...
    def multiplicity(self) -> Any: ...
    def point_group_type(self) -> Any: ...
    def special_op(self) -> Any: ...
    def unique_ops(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

class wyckoff_table:
    def random_site_symmetry(
        self,
        special_position_settings,
        i_position,
        unit_shift_range=...,
        tolerance: float = ...,
    ): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def lookup_index(self, char) -> Any: ...
    def mapping(self, *args, **kwargs) -> Any: ...
    def position(self, *args, **kwargs) -> Any: ...
    def size(self) -> Any: ...
    def space_group_type(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

def fractional_mod_positive(cctbx) -> Any: ...
def fractional_mod_short(cctbx) -> Any: ...
def lattice_symmetry_find_max_delta(*args, **kwargs) -> Any: ...
def lattice_symmetry_group(cctbx) -> Any: ...
def n_fold_operator_from_axis_direction(*args, **kwargs) -> Any: ...
