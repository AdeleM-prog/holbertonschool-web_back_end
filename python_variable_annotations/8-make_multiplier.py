#!/usr/bin/env python3

from typing import Callable
"""Module that defines a function returning a multiplier function."""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.
    Args:
        multiplier: The float value to multiply by.

    Returns:
        A function that takes a float and returns the multiplied result.
    """
    def mult_funct(x: float) -> float:
        return multiplier * x
    return mult_funct
