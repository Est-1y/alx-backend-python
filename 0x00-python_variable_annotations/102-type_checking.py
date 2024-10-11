#!/usr/bin/env python3

"""Type checking
"""

from typing import Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """type checking
    """
    zoomed_in = tuple(
        item for item in lst
        for _ in range(factor)
    ) # type: Tuple[int, ...]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)

