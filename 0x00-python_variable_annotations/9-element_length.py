#!/usr/bin/env python3
""" Complex types - functions """


from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
    This returns a list of tuples where each tuple contains
    an element from the input list
    and its corresponding length.

    Parameters:
    - lst (List[str]): The input list of strings.

    Returns:
    List[Tuple[str, int]]: A list of tuples, each containing
    a string element and its length.
    """
    return [(i, len(i)) for i in lst]
