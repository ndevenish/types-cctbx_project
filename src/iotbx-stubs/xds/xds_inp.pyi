from __future__ import annotations

from typing import Any

class reader:
    def __init__(self) -> None: ...
    @staticmethod
    def is_xds_inp_file(filename): ...
    unit_cell_constants: Any
    minimum_valid_pixel_value: int
    corrections: Any
    trusted_region: Any
    maximum_number_of_processor: int
    fraction_of_polarization: float
    polarization_plane_normal: Any
    starting_angle: float
    oscillation_range: Any
    starting_frame: Any
    include_resolution_range: Any
    space_group_number: int
    max_fac_rmeas: float
    data_range: Any
    sensor_thickness: int
    silicon: Any
    num_segments: int
    segment_orgx: Any
    segment_orgy: Any
    direction_of_segment_x_axis: Any
    direction_of_segment_y_axis: Any
    segment_distance: Any
    segment: Any
    def read_file(self, filename, check_filename: bool = ...) -> None: ...
    untrusted_rectangle: Any
    detector: Any
    overload: Any
    direction_of_detector_x_axis: Any
    direction_of_detector_y_axis: Any
    nx: Any
    ny: Any
    px: Any
    py: Any
    orgx: Any
    orgy: Any
    rotation_axis: Any
    detector_distance: Any
    xray_wavelength: Any
    incident_beam_direction: Any
    friedels_law: Any
    name_template_of_data_frames: Any
    def parse_lines(self, lines) -> None: ...
