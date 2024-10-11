#!/usr/bin/env python3

"""function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """createing and returning a function that multiplies a float
    """
    def multiply(n: float) -> float:
        """multipliying a float
        """
        return n * multiplier
    return multiply
