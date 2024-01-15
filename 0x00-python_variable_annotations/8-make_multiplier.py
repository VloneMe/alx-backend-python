#!/usr/bin/env python3
""" #!/usr/bin/env python3 """


from typing import Callable
called = Callable[[float], float]

def make_multiplier(multiplier: float) -> called:
    """
    This returns a function that multiplies
    a float by the specified multiplier.

    Parameters:
    - multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float and
    returns its product with the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
