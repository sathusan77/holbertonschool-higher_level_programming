#!/usr/bin/python3
"""Module for converting CSV data to JSON format"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format

    Args:
        csv_filename: Name of the CSV file to convert

    Returns:
        True if conversion successful, False otherwise
    """
    try:
        data = []
        
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    
    except FileNotFoundError:
        return False
    except Exception:
        return False
