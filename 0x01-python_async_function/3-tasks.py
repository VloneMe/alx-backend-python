#!/usr/bin/env python3
""" Tasks """

import asyncio
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task for the wait_random coroutine.
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time
