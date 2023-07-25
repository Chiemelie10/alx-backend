#!/usr/bin/env python3
"""This module defines class FIFOCache that inherits from BaseCaching."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class defines the attributes and methods of class
    FIFOCache, a caching system.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        This method adds keys with their coressponding values
        to self.cache_data, the dictionary inherited from the
        parent class.
        """

        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_entered_key = next(iter(self.cache_data))
                del self.cache_data[first_entered_key]
                print("DISCARD: {}".format(first_entered_key))

    def get(self, key):
        """Returns the value in self.cache_data linked to a key."""

        if key is None:
            return None

        value = self.cache_data.get(key)
        return value
