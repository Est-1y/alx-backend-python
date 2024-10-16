#!/usr/bin/env python3

"""100-safe_first_element.py
"""

from typing import List, Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returning an element from the input_list or 'None'
    """

    if lst:
        return lst[0]
    else:
        return None
