#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # Ne pas toucher

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

