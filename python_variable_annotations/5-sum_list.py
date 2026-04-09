#!/usr/bin/env python3
"""Module that defines a function to compute the sum of a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.
    Args:
        input_list: A list of float numbers to be summed.

    Returns:
        The sum of all the floats in the list.
    """
    return sum(input_list)
