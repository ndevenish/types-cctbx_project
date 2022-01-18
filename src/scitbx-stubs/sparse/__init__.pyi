from __future__ import annotations

from typing import Dict, Generator, List, overload

from scitbx.array_family import flex as flex

class vector:
    def as_dense_vector(self) -> flex.double: ...

class matrix:
    @overload
    def __init__(self, rows: int, columns: int) -> None: ...
    @overload
    def __init__(
        self, rows: int, columns: int, elements_by_columns: list[dict[int, float]]
    ) -> None: ...
    @property
    def n_cols(self) -> int: ...
    @property
    def n_rows(self) -> int: ...
    def as_dense_matrix(self) -> flex.double: ...
    def col(self, i: int) -> vector: ...
    def cols(self) -> Generator[vector, None, None]: ...
    @overload
    def assign_block(self, block: matrix, i: int, j: int) -> None: ...
    @overload
    def assign_block(self, block: flex.double, i: int, j: int) -> None: ...

# as_dense_matrix
# clone
# col
# cols
# compact
# is_structural_zero
# is_unit_lower_triangular
# is_upper_triangular
# n_cols
# n_rows
# non_zeroes
# permute_rows
# select_columns
# self_times_diagonal_times_self_transpose
# self_times_symmetric_times_self_transpose
# self_transpose_times_diagonal_times_self
# self_transpose_times_self
# self_transpose_times_symmetric_times_self
# transpose
