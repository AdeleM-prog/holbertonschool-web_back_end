#!/usr/bin/env python3
"""
Module that provides an asynchronous function to execute multiple
coroutines concurrently and collect their results in completion order.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Executes the wait_random coroutine n times concurrently.
    This function schedules n asynchronous tasks using wait_random
    with a maximum delay specified by max_delay. The results are
    collected in the order of completion of each task.
    Args:
        n (int): The number of times to execute the coroutine.
        max_delay (int): The maximum delay value passed to wait_random.

    Returns:
        list[float]: A list of delays returned by each coroutine,
        ordered by completion time.
    """
    tasks = []
    wait_list = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        results = await task
        wait_list.append(results)

    return wait_list
