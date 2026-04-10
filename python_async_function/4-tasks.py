#!/usr/bin/env python3
"""
Module that provides an asynchronous function to execute multiple
tasks concurrently using task_wait_random.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times concurrently.
    This function creates n tasks using task_wait_random and returns
    the list of results in the order of completion.
    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task.
    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = []
    wait_list = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        results = await task
        wait_list.append(results)

    return wait_list