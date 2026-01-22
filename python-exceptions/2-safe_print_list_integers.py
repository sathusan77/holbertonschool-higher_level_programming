#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers of a list and return the number printed."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print()
    return count
