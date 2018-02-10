"""
Unit tests for base_model
"""
import unittest
import json
import sys
import io
import os
import uuid
import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """This class contains unit tests for the BaseModel class."""
    def test_file_storage_creation(self):
        """This create an instance of FileStorage"""
        test = FileStorage()
        self.assertIsInstance(test, FileStorage)

    def test_file_storage_all(self):
        """Test to see that all returns a dict"""
        test = FileStorage()
        temp = test.all()
        self.assertIsInstance(temp, dict)

    def test_file_storage_new(self):
        """Test to see that new sets object in __objects with new key"""
        test = FileStorage()
        temp = BaseModel()
        test.new(temp)
        test_dict = test.all()
        test_entry = temp.__class__.__name__ + "." + temp.id
        self.assertIn(test_entry, test_dict)

    def test_file_storage_save(self):
        """Test to see that file.json is created"""
        test = FileStorage()
        test.save()
        try:
            os.path.exists('file.json')
        except FileNotFoundError as error:
            print(error)

    #TODO Look into mocking objects for this test
    def test_file_storage_data_check(self):
        """Test to see JSON data is written as string to file"""
        test_read = ""
        with open('file.json', 'r') as fp:
            test_read = fp.read()
        self.assertIsInstance(test_read, str)

    #TODO Look into mocking object for this test
    def test_file_storage_reload(self):
        """Test to see reload successfully reloads JSON file into __objects"""
        test = FileStorage()
        test.reload()
        test_dict = test.all()
        self.assertIsInstance(test_dict, dict)
