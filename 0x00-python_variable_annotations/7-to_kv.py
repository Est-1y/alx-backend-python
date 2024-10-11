#!/usr/bin/env python3

"""string int/float tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returning a tuple
    """
    return (k, v ** 2)
