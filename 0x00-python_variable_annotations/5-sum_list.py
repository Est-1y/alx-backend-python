#!/usr/bin/env python3

""" Sum list
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """returning the sum of floats
    """
    sum = 0.0

    for num in input_list:
        if isinstance(num, float):
            sum += num

    return sum
