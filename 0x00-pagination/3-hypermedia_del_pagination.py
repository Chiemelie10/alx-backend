#!/usr/bin/env python3
"""This module defines class Server"""

import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns a tuple of size two containing
    a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    page_range = (start_index, end_index)

    return page_range


class Server():
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""

        if self.__dataset is None:
            with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the required pages"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        if page > total_pages:
            return []

        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[
                  str, Union[int, List[List], None]]:
        """This method returns a dictionary containg info about the api"""

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        required_data = self.get_page(page, page_size)
        page_size = len(required_data)

        if page == 1:
            prev_page = None
            next_page = page + 1
        elif page > 1 and page < total_pages:
            next_page = page + 1
            prev_page = page - 1
        elif page >= total_pages:
            next_page = None
            prev_page = page - 1

        return {
            'page_size': page_size,
            'page': page,
            'data': required_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""

        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Union[int, None] = None,
                        page_size: int = 10) -> Dict:
        """
        This method uses index to return the requested page,
        ensuring if certain rows are removed from the dataset,
        the user does not miss items from dataset when changing page.
        """

        dataset = self.indexed_dataset()

        if index is not None:
            assert isinstance(index, int) and index >= 0\
                and index < len(dataset)
            assert isinstance(page_size, int) and page_size >= 0\
                and page_size < len(dataset)

            deleted_data = []
            for i in range(index, index + page_size):
                if dataset.get(i) is None:
                    deleted_data.append(dataset.get(i))
                    continue

            if len(deleted_data) == 0:
                data = [dataset.get(i) for i in range(index,
                                                      index + page_size)]
                next_index = index + page_size
            else:
                data = []

                for i in range(index, index + page_size + len(deleted_data)):
                    if dataset.get(i) is None:
                        continue
                    data.append(dataset.get(i))

                next_index = index + page_size + len(deleted_data)

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
