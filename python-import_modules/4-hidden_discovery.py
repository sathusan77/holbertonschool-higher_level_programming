#!/usr/bin/python3
"""
Lists all names defined in the compiled module hidden_4.pyc
"""

import marshal

if __name__ == "__main__":
    # Load the compiled .pyc file
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)  # Skip header
        code = marshal.load(f)

    # Extract names and filter
    names = [n for n in code.co_names if not n.startswith("__")]

    # Print in alphabetical order
    for name in sorted(names):
        print(name)
