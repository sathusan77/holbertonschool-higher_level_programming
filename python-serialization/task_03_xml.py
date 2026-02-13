#!/usr/bin/python3
"""Module for XML serialization and deserialization"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save to file

    Args:
        dictionary: Python dictionary to serialize
        filename: Name of the XML file to create
    """
    root = ET.Element('data')
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file to Python dictionary

    Args:
        filename: Name of the XML file to read

    Returns:
        Python dictionary with deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary
