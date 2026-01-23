#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

values = [89, -89, "School", 3.14, None]

for value in values:
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

