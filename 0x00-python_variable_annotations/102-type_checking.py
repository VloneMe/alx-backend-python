#!/usr/bin/env python3
""" Type Checking """


from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)

array = (12, 72, 91)

zoom_2x = zoom_array(array)

# This line will produce a mypy error
zoom_3x = zoom_array(array, 3.0)
