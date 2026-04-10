#!/usr/bin/env python3
"""
Module that provides a coroutine to collect random numbers
using an async comprehension.
"""

import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator.
    Returns:
        list[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
