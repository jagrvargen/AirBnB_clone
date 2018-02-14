#!/usr/bin/python3
"""
Unit tests for review
"""
import unittest
import json
import sys
import io
import uuid
import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """This class contains unit tests for the Review class."""

    def test_review_is_instance(self):
        """Set up an instance of a Review."""
        base = Review()
        self.assertIsInstance(base, Review)

    def test_review_has_placeid(self):
        """check if review has place_id"""
        base = Review()
        self.assertIsInstance(base.place_id, str)
        self.assertTrue(hasattr(base, "place_id"))

    def test_review_has_userid(self):
        """check if review has user_id"""
        base = Review()
        self.assertIsInstance(base.user_id, str)
        self.assertTrue(hasattr(base, "user_id"))


    def test_review_has_text(self):
        """check if review has text"""
        base = Review()
        self.assertIsInstance(base.text, str)
        self.assertTrue(hasattr(base, "text"))
