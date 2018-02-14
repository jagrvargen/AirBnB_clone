#!/usr/bin/python3
"""
Unit tests for user
"""
import unittest
import json
import sys
import io
import uuid
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """This class contains unit tests for the User class."""
    def test_user_is_instance(self):
        """Set up an instance of a User."""
        base = User()
        self.assertIsInstance(base, User)

    def test_user_verify(self):
        """Test that User object has id, created_at, updated_at"""
        base = User()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_user_has_firstname(self):
        """checks for first_name attribute"""
        base = User()
        self.assertTrue(hasattr(base, "first_name"))
        self.assertIsInstance(base.first_name, str)

    def test_user_has_lastname(self):
        """checks for last_name attribute"""
        base = User()
        self.assertTrue(hasattr(base, "last_name"))
        self.assertIsInstance(base.last_name, str)

    def test_user_has_email(self):
        """checks for email attribute"""
        base = User()
        self.assertTrue(hasattr(base, "email"))
        self.assertIsInstance(base.email, str)

    def test_user_has_password(self):
        """checks for password attribute"""
        base = User()
        self.assertTrue(hasattr(base, "password"))
        self.assertIsInstance(base.password, str)

    def test_create_dict(self):
        """Test that to_dict creates a dictionary."""
        base = User()
        user_dict = base.to_dict()
        self.assertTrue(type(user_dict), dict)
        self.assertIsInstance(user_dict, dict)
        for attr in base.__dict__:
            self.assertTrue(attr in user_dict)
            self.assertTrue("__class__" in user_dict)
