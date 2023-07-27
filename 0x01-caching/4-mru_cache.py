#!/usr/bin/env python3
"""This module defines class MRUCache that inherits from BaseCaching."""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    This class defines the attributes and methods of class
    LRUCache, a caching system.
    """

    def __init__(self):
        super().__init__()
        self.tracker = {}
        self.tracker_list = []

    def put(self, key, item):
        """
        This method adds keys with their coressponding values
        to self.cache_data, the dictionary inherited from the
        parent class. It also deletes the least recent used key
        when the cache reaches full capacity.
        """

        if key is not None and item is not None:
            self.cache_data[key] = item

            if key in self.tracker_list:
                self.tracker_list.remove(key)

            self.tracker_list.append(key)

            if key not in self.tracker.keys():
                self.tracker[key] = 0

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                count = 0

                for key, value in self.tracker.items():
                    if count == 0:
                        highest = value
                        key_to_highest = key
                        count += 1
                        continue
                    if value > highest:
                        highest = value
                        key_to_highest = key

                highest_value_keys = []

                for key, value in self.tracker.items():
                    if value == highest:
                        highest_value_keys.append(key)

                if len(highest_value_keys) == len(self.tracker):
                    list_iteration_object = reversed(self.tracker_list)

                    for _ in range(2):
                        key = next(list_iteration_object)

                    self.tracker_list.remove(key)
                    del self.tracker[key]
                    del self.cache_data[key]
                else:
                    length = len(self.tracker_list)

                    list_iteration_object = reversed(self.tracker_list)

                    for _ in range(length):
                        key = next(list_iteration_object)
                        if key in highest_value_keys:
                            break

                    self.tracker_list.remove(key)
                    del self.tracker[key]
                    del self.cache_data[key]

                print("DISCARD: {}".format(key))

                for key in self.tracker.keys():
                    self.tracker[key] = 0

    def get(self, key):
        """Returns the value in self.cache_data linked to a key."""

        if key is None:
            return None

        value = self.cache_data.get(key)

        if value is not None:
            self.tracker[key] = 1

        return value
