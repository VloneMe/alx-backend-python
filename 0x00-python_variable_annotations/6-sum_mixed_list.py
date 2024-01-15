#!/usr/bin/env pytho3
""" Complex types - mixed list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This returns the sum of a list of integers and floats.

    Parameters:
    - mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
    float: The sum of the input list.
    """
    return float(sum(mxd_lst))
