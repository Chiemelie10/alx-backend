#!/usr/bin/env python3
"""This module defines class LRUCache that inherits from BaseCaching."""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This class defines the attributes and methods of class
    LRUCache, a caching system.
    """

    def __init__(self):
        super().__init__()
        self.tracker = {}
        self.tracker_list = []
        self.insertions_after_get = {}

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
                        lowest = value
                        key_to_lowest = key
                        continue
                    if value < lowest:
                        lowest = value
                        key_to_lowset = key

                lowest_value_keys = []

                for key, value in self.tracker.items():
                    if value == lowest:
                        lowest_value_keys.append(key)

                length = len(self.tracker_list)

                list_iteration_object = iter(self.tracker_list)

                for _ in range(length):
                    key = next(list_iteration_object)
                    if key in lowest_value_keys:
                        break

                self.tracker_list.remove(key)
                del self.tracker[key]
                del self.cache_data[key]

                print("DISCARD: {}".format(key))

                keys_to_delete_from_insertion_dict = []

                for key, value in self.insertions_after_get.items():
                    self.insertions_after_get[key] = value + 1
                    if value == 3:
                        keys_to_delete_from_insertion_dict.append(key)

                for key in self.tracker.keys():
                    number_of_gets = self.insertions_after_get.get(key)
                    if number_of_gets == 3:
                        self.tracker[key] = 0

                for key in keys_to_delete_from_insertion_dict:
                    del self.insertions_after_get[key]

    def get(self, key):
        """Returns the value in self.cache_data linked to a key."""

        if key is None:
            return None

        value = self.cache_data.get(key)

        if value is not None:
            # current_value = self.tracker.get(key)
            self.tracker[key] = 1
            self.insertions_after_get[key] = 1

        return value
