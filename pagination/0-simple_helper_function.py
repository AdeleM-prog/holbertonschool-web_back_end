#!/usr/bin/env python3

""""""

def index_range (page, page_size):
    offset = (page - 1) * page_size
    end_index = offset + page_size
    return (offset, end_index)
