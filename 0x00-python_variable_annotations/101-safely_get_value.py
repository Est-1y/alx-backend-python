#!/usr/bin/env python3
"""getting value
"""

from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[Union[T, None]] = None
                     ) -> Union[Any, T]:
    """value
    """
    if key in dct:
        return dct[key]
    else:
        return default
