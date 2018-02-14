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
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

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
        """Test the __str__ method's types"""
        base = BaseModel()
        t1 = base.__class__.__name__
        t2 = base.id
        t3 = base.__dict__
        self.assertIsInstance(t1, str)
        self.assertIsInstance(t2, str)
        self.assertDictEqual(t3, base.__dict__)

    def test_base_str_method(self):
        """Test the __str__ method for BaseModel"""
        base = BaseModel()
        test = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(str(base), test)

    def test_save(self):
        """updates public instnace updated_at with current datetime"""
        base = BaseModel()
        id1 = base.updated_at
        base.save()
        self.assertNotEqual(id1, base.updated_at)

    def test_is_instance_dict(self):
        """Check that to_dict returns an instance if a dict."""
        base = BaseModel()
        b1 = base.to_dict()
        self.assertIsInstance(b1, dict)

    def test_to_dict_datetime(self):
        """tests that datetime is converted to string"""
        base = BaseModel()
        b1 = base.to_dict()
        created = b1["created_at"]
        updated = b1["updated_at"]
        self.assertIsInstance(created, str)
        self.assertIsInstance(updated, str)

    def test_to_dict_class_string(self):
        """tests that __class__ is inserted using to_dict"""
        base = BaseModel()
        b1 = base.to_dict()
        test = b1["__class__"]
        self.assertIsInstance(test, str)

    def test_to_dict_output(self):
        """tests that output written properly using to_dict"""
        base = BaseModel()
        b1 = base.to_dict()
        self.assertIsInstance(b1, dict)
        self.assertIsInstance(b1["created_at"], str)
        self.assertIsInstance(b1["updated_at"], str)

    def test_basemodel_from_dict(self):
        """test the recreation of instance with dict representation"""
        base = BaseModel()
        test = base.to_dict()
        base2 = BaseModel(**test)
        self.assertDictEqual(base.__dict__, base2.__dict__)
