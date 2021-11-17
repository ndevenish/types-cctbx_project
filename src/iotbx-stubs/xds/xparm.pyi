from typing import Any, Optional

class reader:
    @staticmethod
    def find_version(filename): ...
    @staticmethod
    def is_xparm_file(filename, check_filename: bool = ...): ...
    def read_file(self, filename, check_filename: bool = ...) -> None: ...
    starting_frame: Any
    starting_angle: Any
    oscillation_range: Any
    rotation_axis: Any
    wavelength: Any
    beam_vector: Any
    num_segments: int
    detector_size: Any
    pixel_size: Any
    detector_distance: Any
    detector_origin: Any
    detector_x_axis: Any
    detector_y_axis: Any
    detector_normal: Any
    space_group: Any
    unit_cell: Any
    unit_cell_a_axis: Any
    unit_cell_b_axis: Any
    unit_cell_c_axis: Any
    def parse_version_1_tokens(self, tokens) -> None: ...
    segments: Any
    orientation: Any
    def parse_version_2_tokens(self, tokens) -> None: ...

class writer:
    num_segments: int
    segments: Any
    orientation: Any
    def __init__(
        self,
        starting_frame,
        starting_angle,
        oscillation_range,
        rotation_axis,
        wavelength,
        beam_vector,
        space_group,
        unit_cell,
        unit_cell_a_axis,
        unit_cell_b_axis,
        unit_cell_c_axis,
        num_segments,
        detector_size,
        pixel_size,
        detector_origin,
        detector_distance,
        detector_x_axis,
        detector_y_axis,
        detector_normal,
        segments: Optional[Any] = ...,
        orientation: Optional[Any] = ...,
    ) -> None: ...
    def show(self, out: Optional[Any] = ...) -> None: ...
    def write_file(self, filename) -> None: ...

xparm_xds_template: str
xparm_xds_segment_template: Any

def write(
    starting_frame,
    starting_angle,
    oscillation_range,
    rotation_axis,
    wavelength,
    beam_vector,
    space_group,
    unit_cell,
    unit_cell_a_axis,
    unit_cell_b_axis,
    unit_cell_c_axis,
    num_segments,
    detector_size,
    pixel_size,
    detector_origin,
    detector_distance,
    detector_x_axis,
    detector_y_axis,
    detector_normal,
    segments: Optional[Any] = ...,
    orientation: Optional[Any] = ...,
): ...
