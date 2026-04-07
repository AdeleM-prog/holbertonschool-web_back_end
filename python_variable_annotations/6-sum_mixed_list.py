#!/usr/bin/env python3

from typing import List, Union
"""Module that defines a function to compute the sum of a list of
integers and floats."""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list containing integers and floats.
    Args:
        mxd_lst: A list of integers and floats to be summed.

    Returns:
        The sum of all elements in the list as a float.
    """

    return sum(mxd_lst)
