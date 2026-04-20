#!/usr/bin/env python3

"""Helper function for pagination."""


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): the page number (1-indexed)
        page_size (int): the number of items per page

    Returns:
        tuple: a tuple (start_index, end_index)
    """
    offset = (page - 1) * page_size
    end_index = offset + page_size
    return (offset, end_index)
