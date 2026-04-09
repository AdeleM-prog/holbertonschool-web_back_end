#!/usr/bin/env python3
"""Module that defines a function to map a string to a squared value."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number as float.
    Args:
        k: The string key.
        v: An int or float value.

    Returns:
        A tuple with the string and the squared value as float.
    """
    v = float(v * v)
    return (k, v)
