#!/usr/bin/env python3
""" Complex types - list of floats """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This returns the sum of a list of floats.

    Parameters:
    - input_list (List[float]): The list of floats.

    Returns:
    float: The sum of the input list.
    """
    return sum(input_list)
