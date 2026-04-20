#!/usr/bin/env python3
"""Module for paginating a database of popular baby names."""

import csv
from typing import List


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset, loading it from CSV if necessary."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.

        Args:
            page (int): the page number (1-indexed, default 1)
            page_size (int): the number of items per page (default 10)

        Returns:
            List[List]: the list of rows for the requested page,
            or an empty list if the page is out of range
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        offset, end_index = index_range(page, page_size)
        return self.dataset()[offset:end_index]
