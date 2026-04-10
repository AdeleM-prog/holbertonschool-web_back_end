#!/usr/bin/env python3
"""
Module that provides an asynchronous generator.
"""

import asyncio
import random


async def async_generator():
    """
    Yields random numbers between 0 and 10 asynchronously.

    This generator produces 10 random float values, waiting
    1 second between each yield.

    Yields:
        float: A random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
