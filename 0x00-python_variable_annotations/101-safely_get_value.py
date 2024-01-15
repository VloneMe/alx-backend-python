#!/usr/bin/env python3
""" More involved type annotations """

from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on the given key.

    Parameters:
    - dct (Mapping): The input dictionary.
    - key (Any): The key to look for in the dictionary.
    - default (Union[T, None]): The default value to return
    if the key is not present. Defaults to None.

    Returns:
    Union[Any, T]: The value corresponding to the key if it exists,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
