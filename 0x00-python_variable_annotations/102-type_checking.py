#!/usr/bin/env python3
"""Module to return a zoomed array with repeated
elements based on a factor."""

from typing import List, Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """Return a list where each element in the input
    tuple is repeated 'factor' times."""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
