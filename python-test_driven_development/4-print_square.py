#!/usr/bin/python3
"""Defines a function that prints a square with the character #."""

def print_square(size):
    """Print a square of given size using #.

    size must be an integer >= 0, otherwise raises TypeError or ValueError.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)

