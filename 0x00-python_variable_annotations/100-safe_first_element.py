#!/usr/bin/env python3
""" The types of the elements of the input are not know """

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This returns the first element of a list if it exists,
    otherwise returns None.

    Parameters:
    - lst (list): The input list.

    Returns:
    Optional[Any]: The first element of the list if it exists,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
