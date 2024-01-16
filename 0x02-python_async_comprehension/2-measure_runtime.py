#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions """


import asyncio
from time import time


async def measure_runtime() -> float:
    """
    Measure Runtime

    Executes async_comprehension four times in parallel using asyncio.gather
    and measures the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()
    total_runtime = end_time - start_time
    return total_runtime
