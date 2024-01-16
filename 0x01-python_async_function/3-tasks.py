#!/usr/bin/env python3
""" Tasks """

import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This regular function that takes an integer max_delay
    and returns an asyncio.Task.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task for the wait_random coroutine.
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
