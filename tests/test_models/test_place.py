#!/usr/bin/python3
"""
Unit tests for place
"""
import unittest
import json
import sys
import io
import uuid
import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """This class contains unit tests for the Place class."""

    def test_is_instance(self):
        """Set up an instance of a Place."""
        base = Place()
        self.assertIsInstance(base, Place)
