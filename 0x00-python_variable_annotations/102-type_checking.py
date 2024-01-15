#!/usr/bin/env python3
""" Type Checking """

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array by duplicating each element 'factor' times.

    Parameters:
    - lst (Tuple): The input tuple to be zoomed.
    - factor (int): The factor by which each element should be duplicated. Defaults to 2.

    Returns:
    - List: The zoomed-in list containing each element duplicated 'factor' times.
    """
    
    """ Creating a list comprehension to zoom in on the input tuple """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

""" Input array """
array = (12, 72, 91)

""" Zooming in with the default factor (2x) """
zoom_2x = zoom_array(array)

""" Zooming in with a custom factor (3x) """
zoom_3x = zoom_array(array, 3)
