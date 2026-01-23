#!/usr/bin/python3
"""Defines a function that adds two integers."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    a and b must be integers or floats, otherwise raise a TypeError.
    Floats are casted to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

