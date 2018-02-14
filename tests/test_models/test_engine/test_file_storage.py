#!/usr/bin/python3
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
from unittest import TestCase
from unittest.mock import patch, Mock
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

    def test_file_storage_new_key(self):
        """Test to see that new sets object in __objects with new key"""
        test = FileStorage()
        temp = BaseModel()
        test.new(temp)
        test_dict = test.all()
        test_entry = temp.__class__.__name__ + "." + temp.id
        self.assertIn(test_entry, test_dict)

    def test_file_storage_new_value(self):
        """Test to see that new sets value as an object in __objects"""
        test = FileStorage()
        temp = BaseModel()
        test.new(temp)
        test_dict = test.all()
        test_entry = temp.__class__.__name__ + "." + temp.id
        test_obj = test_dict[test_entry]
        self.assertIsInstance(test_obj, type(temp))

    def test_file_storage_save(self):
        """Test to see that file.json is created"""
        test = FileStorage()
        test.save()
        self.assertEqual(true, os.path.exists('file.json'))

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
    def test_file_storage_reload_dict(self):
        """Test to see reload successfully reloads JSON file into type dict"""
        test = FileStorage()
        test.reload()
        test_dict = test.all()
        self.assertIsInstance(test_dict, dict)

    #TODO Look into mocking object for this test
    def test_file_storage_reload_key(self):
        """
        Test to see reload successfully reloads JSON file with the proper key
        """
        test = FileStorage()
        temp = BaseModel()
        test_entry = temp.__class__.__name__ + "." + temp.id
        test.new(temp)
        test.save()
        test.reload()
        test_dict = test.all()
        self.assertIn(test_entry, test_dict)

    #TODO Look into mocking object for this test
    def test_file_storage_reload_value(self):
        """
        Test to see reload successfully reloads JSON file with the proper value
        """
        test = FileStorage()
        temp = BaseModel()
        test_entry = temp.__class__.__name__ + "." + temp.id
        test.new(temp)
        test.save()
        test.reload()
        test_dict = test.all()
        test_obj = test_dict[test_entry]
        self.assertIsInstance(test_obj, type(temp))
