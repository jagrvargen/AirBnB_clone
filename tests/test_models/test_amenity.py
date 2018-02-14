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

    def test_is_instance(self):
        """Set up an instance of a Amenity."""
        base = Amenity()
        self.assertIsInstance(base, Amenity)