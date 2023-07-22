#!/usr/bin/env python3
"""Test module for 0-simple_helper_function.py"""

index_rage = __import__('0-simple_helper_function').index_range

pages = index_rage(1, 7)
print(type(pages))
print(pages)

pages = index_rage(3, 15)
print(type(pages))
print(pages)
