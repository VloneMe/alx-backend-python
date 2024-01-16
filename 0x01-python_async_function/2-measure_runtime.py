#!/usr/bin/env python3
""" Measure the runtime """


import time
from typing import List
from random_delay_module import wait_n  # Replace with the actual module name


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    This measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of iterations for wait_n.
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: Average time per iteration.
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time
