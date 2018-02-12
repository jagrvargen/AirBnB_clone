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

    def test_is_instance(self):
        """Set up an instance of a User."""
        base = User()
        self.assertIsInstance(base, User)
