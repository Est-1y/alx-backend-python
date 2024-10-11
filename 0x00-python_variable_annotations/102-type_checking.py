#!/usr/bin/env python3
'''type checking`
'''
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    '''type checking
    '''
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]  # type: List[int]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)
