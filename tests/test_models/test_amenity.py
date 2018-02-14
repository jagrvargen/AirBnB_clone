#!/usr/bin/python3
"""
Unit tests for amenity
"""
import unittest
import json
import sys
import io
import uuid
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """This class contains unit tests for the Amenity class."""

    def test_amenity_is_instance(self):
        """Set up an instance of a Amenity."""
        base = Amenity()
        self.assertIsInstance(base, Amenity)

    def test_amentiy_has_name(self):
        """make sure Amenity has name"""
        base = Amenity()
        self.assertTrue(hasattr(base, "name"))
