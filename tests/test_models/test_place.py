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

    def test_place_is_instance(self):
        """Set up an instance of a Place."""
        base = Place()
        self.assertIsInstance(base, Place)

    def test_place_has_cityid(self):
        """checks for city_id"""
        base = Place()
        self.assertTrue(hasattr(base, "city_id"))

    def test_place_has_userid(self):
        """checks for user_id"""
        base = Place()
        self.assertTrue(hasattr(base, "user_id"))

    def test_place_has_name(self):
        """checks for name"""
        base = Place()
        self.assertTrue(hasattr(base, "name"))

    def test_place_has_description(self):
        """checks for description"""
        base = Place()
        self.assertTrue(hasattr(base, "description"))

    def test_place_has_numberroom(self):
        """checks for number_room"""
        base = Place()
        self.assertTrue(hasattr(base, "number_rooms"))

    def test_place_has_numberbath(self):
        """checks for numbers_bathrooms"""
        base = Place()
        self.assertTrue(hasattr(base, "number_bathrooms"))

    def test_place_has_maxguest(self):
        """checks for max_guest"""
        base = Place()
        self.assertTrue(hasattr(base, "max_guest"))

    def test_place_has_pricenight(self):
        """checks for price_by_night"""
        base = Place()
        self.assertTrue(hasattr(base, "price_by_night"))

    def test_place_has_latitude(self):
        """checks for latitude"""
        base = Place()
        self.assertTrue(hasattr(base, "latitude"))

    def test_place_has_longitude(self):
        """checks for longitude"""
        base = Place()
        self.assertTrue(hasattr(base, "longitude"))

    def test_place_has_amenityid(self):
        """checks for amenity_ids"""
        base = Place()
        self.assertTrue(hasattr(base, "amenity_ids"))
