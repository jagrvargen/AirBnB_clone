"""
Unit tests for base_model
"""
import unittest
import json
import sys
import io
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
        """Test to see that all reteurns a dict"""
        test = FileStorage()
        temp = test.all()
        self.assertIsInstance(temp, dict)

    def test_file_storage_new(self):
        """Test to see that new sets object in __objects with new key"""
        test = FileStorage()
        temp = BaseModel()
        test.new(temp)
        self.assertIsInstance(temp, dict)
