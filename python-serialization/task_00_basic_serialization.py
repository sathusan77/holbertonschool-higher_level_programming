#!/usr/bin/python3
"""Module for basic serialization and deserialization"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file

    Args:
        data: Python dictionary with data
        filename: The filename of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserialize JSON file to recreate Python dictionary

    Args:
        filename: The filename of the input JSON file

    Returns:
        Python dictionary with deserialized JSON data
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
