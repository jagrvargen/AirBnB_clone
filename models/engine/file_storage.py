#!/usr/bin/python3
"""Module for file storage"""
import json


class FileStorage():
    """
    FileStorage - class in charge of serializing and deserializing files
                  to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """set entries in dict __objects with key <obj class name>.id"""
        new_dict = obj.to_dict()
        new_key = obj.__class__.__name__ + "." + obj.id
        #self.__objects[new_key] = new_dict
        self.__objects[new_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file path)"""
        temp = {}
        with open(self.__file_path, "w", encoding="utf-8") as fp:
            for key, value in self.__objects.items():
                temp[key] = value.to_dict()
            json.dump(temp, fp)

    def reload(self):
        """deserializes the JSON file to __objects (only if file exists"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                d = json.load(fp)
            from models.base_model import BaseModel
            from models.user import User
            for key, value in d.items():
                if key[0:9] == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                elif key[0:4] == "User":
                    self.__objects[key] = User(**value)
        except FileNotFoundError as error:
            pass
