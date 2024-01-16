#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Asynchronous Generator

    Yields:
        int: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
