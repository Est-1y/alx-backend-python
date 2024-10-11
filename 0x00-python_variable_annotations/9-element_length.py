#!/usr/bin/env python3

"""Function parameters returning values
"""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returning length
    """
    return [(i, len(i)) for i in lst]
