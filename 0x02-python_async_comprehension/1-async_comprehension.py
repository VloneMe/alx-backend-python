#!/usr/bin/env python3
""" Async comprenhesion gen """

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous Comprehension

    Collects 10 random numbers using an asynchronous comprehension over async_generator.

    Returns:
        List[int]: List of 10 random numbers.
    """
    return ([i async for i in async_generator()])
