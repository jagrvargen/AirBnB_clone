#!/usr/bin/python3
"""Module for file storage"""
import json


class FileStorage():
    """
    FileStorage - class in charge of serializing and deserializing files
                  to instances
    """
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """set entries in dict __objects with key <obj class name>.id"""
        pass

    def save(self):
        """serializes __objects to the JSON file (path: __file path)"""
        pass

    def reload(self):
        """deserializes the JSON file to __objects (only if file exists"""
        pass
