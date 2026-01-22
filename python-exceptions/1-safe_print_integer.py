#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer and return True if successful, False otherwise."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
