#!/usr/bin/env python3
"""This module defines a function index_range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns a tuple of size two containing
    a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    page_range = (start_index, end_index)

    return page_range
