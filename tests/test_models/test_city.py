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

    def test_city_is_instance(self):
        """Set up an instance of a City."""
        base = City()
        self.assertIsInstance(base, City)

    def test_city_has_stateid(self):
        """check if city has state_id"""
        base = City()
        self.assertIsInstance(base.state_id, str)
        self.assertTrue(hasattr(base, "state_id"))


    def test_city_has_name(self):
        """check if city has name"""
        base = City()
        self.assertIsInstance(base.name, str)
        self.assertTrue(hasattr(base, "name"))
