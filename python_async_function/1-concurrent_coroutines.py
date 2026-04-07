#!/usr/bin/env python3

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    tasks = []
    wait_list = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        results = await task
        wait_list.append(results)

    return wait_list
