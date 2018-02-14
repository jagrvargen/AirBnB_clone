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

    def test_user_has_firstname(self):
        """checks for first_name attribute"""
        base = User()
        self.assertTrue(hasattr(base, "first_name"))

    def test_user_has_lastname(self):
        """checks for last_name attribute"""
        base = User()
        self.assertTrue(hasattr(base, "last_name"))

    def test_user_has_email(self):
        """checks for email attribute"""
        base = User()
        self.assertTrue(hasattr(base, "email"))

    def test_user_has_password(self):
        """checks for password attribute"""
        base = User()
        self.assertTrue(hasattr(base, "password"))
