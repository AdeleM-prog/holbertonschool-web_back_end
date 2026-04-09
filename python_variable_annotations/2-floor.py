#!/usr/bin/env python3
"""Module that provides a function to compute the floor of a float."""


import math


def floor(n: float) -> int:
    """Return the floor of a floating point number.
    Args:
        n: The float number to floor.
    Returns:
        The largest integer less than or equal to n.
    """
    return math.floor(n)
