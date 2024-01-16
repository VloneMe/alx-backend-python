#!/usr/bin/env python3

import asyncio
from typing import List
import rando

task_wait_random = __import__('3-tasks').wait_random

m
async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
