#!/usr/bin/env python3
"""This module defines class LIFOCache that inherits from BaseCaching."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This class defines the attributes and methods of class
    LIFOCache, a caching system.
    """

    def __init__(self):
        super().__init__()
        self.tracker = []

    def put(self, key, item):
        """
        This method adds keys with their coressponding values
        to self.cache_data, the dictionary inherited from the
        parent class. It also deletes the last inserted key
        when the cache reaches full capacity.
        """

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.tracker.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                list_reverse_iter_object = reversed(self.tracker)

                for _ in range(2):
                    second_to_last_key = next(list_reverse_iter_object)

                self.tracker.remove(second_to_last_key)

                del self.cache_data[second_to_last_key]
                print("DISCARD: {}".format(second_to_last_key))

    def get(self, key):
        """Returns the value in self.cache_data linked to a key."""

        if key is None:
            return None

        value = self.cache_data.get(key)
        return value
