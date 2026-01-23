#!/usr/bin/python3
"""This module provides a function to add two integers."""

def add_integer(a, b=98):
    """Return the addition of two integers a and b.
    
    a and b must be integers or floats (floats are casted to integers).
    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

