#!/usr/bin/python3
"""
Unit tests for city
"""
import unittest
import json
import sys
import io
import uuid
import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """This class contains unit tests for the City class."""

    def test_is_instance(self):
        """Set up an instance of a City."""
        base = City()
        self.assertIsInstance(base, City)
