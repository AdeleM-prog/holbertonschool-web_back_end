#!/usr/bin/env python3
"""Module that defines a function returning elements and their lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each element and its length.
    Args:
        lst: An iterable of sequences.

    Returns:
        A list of tuples containing each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
