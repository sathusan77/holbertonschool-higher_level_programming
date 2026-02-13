#!/usr/bin/python3
"""Module for pickling custom objects"""


import pickle


class CustomObject:
    """Custom class for serialization with pickle"""

    def __init__(self, name, age, is_student):
        """
        Initialize CustomObject

        Args:
            name: String representing the name
            age: Integer representing the age
            is_student: Boolean indicating if student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance to a file

        Args:
            filename: Name of the file to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file

        Args:
            filename: Name of the file to load the object from

        Returns:
            Instance of CustomObject or None if error
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
