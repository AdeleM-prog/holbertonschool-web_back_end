#!/usr/bin/env python3
"""module that provides a function to measure the execution time of
a process"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of the wait_n function.
    This function records the start time, executes wait_n with the
    provided arguments, and then calculates and returns the total
    time taken for the execution.
    Args:
        n (int): The number of times to execute the coroutine.
        max_delay (int): The maximum delay value passed to wait_n.
    Returns:
        float: The average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time-start_time)/n
