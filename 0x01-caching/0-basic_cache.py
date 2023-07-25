#!/usr/bin/env python3
"""This module defines class BasicCache that inherits from BaseCaching."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class defines the attributes and methods of class BasicCache,
    a caching system.
    """

    def put(self, key, item):
        """Adds key and corresponding item to the cache."""

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """This method returns the value in self.cache_data linked to key."""

        value = self.cache_data.get(key)

        return value
