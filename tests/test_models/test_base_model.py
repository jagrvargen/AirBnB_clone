"""
Unit tests for base_model
"""
import unittest
import json
import sys
import io
import uuid
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class contains unit tests for the BaseModel class."""

    def setUp(self):
        """Set up an instance of a BaseModel."""
        base = BaseModel()

    def tearDown(self):
        """Delete the instance of base."""
        del self

    def test_base_instance(self):
        """Tests if BaseModel instance is created. """
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_base_model_id(self):
        """Tests if the id is properly assigned to an instance."""
        base = BaseModel()
        self.assertIsInstance(base.id, str)

    def test_created_at(self):
        """Tests the instantiation time"""
        base = BaseModel()
        self.assertIsInstance(base.created_at, datetime.date)

    def test_updated_at(self):
        """Tests the updated time"""
        base = BaseModel()
        self.assertIsInstance(base.updated_at, datetime.date)

    def test_base_str(self):
        """Test the __str__ method for BaseModel"""
        base = BaseModel()
        t1 = base.__name__
        t2 = base.id
        t3 = base.__dict__
        self.assertIsInstance(base.t1, str)
        self.assertIsInstance(base.t2, str)
        self.assertDictEqual(base.t3, base.__dict__)
