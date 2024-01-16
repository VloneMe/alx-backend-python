#!/usr/bin/env python3
""" Async Comprehensions """


from typing import List

async def async_comprehension() -> List[int]:
    """
    This asynchronous Comprehension

    Collects 10 random numbers using an asynchronous 
    comprehension over async_generator.

    Returns:
        List[int]: List of 10 random numbers.
    """
    return [i async for i in async_generator()]
