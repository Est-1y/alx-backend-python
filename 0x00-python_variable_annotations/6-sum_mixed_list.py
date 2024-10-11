#!/usr/bin/env python3

""" Sum of a mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returning the sum of a list
    """
    mxd_sum = 0.0

    for idx in mxd_list:
        if isinstance(idx, int) or isinstance(idx, float):
            mxd_sum += idx

    return mxd_sum
