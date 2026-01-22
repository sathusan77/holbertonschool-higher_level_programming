#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Return the sum of all unique integers in a list."""
    unique_numbers = set(my_list)  # convertit la liste en ensemble (unique)
    return sum(unique_numbers)
