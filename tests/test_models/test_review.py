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

    def test_is_instance(self):
        """Set up an instance of a Review."""
        base = Review()
        self.assertIsInstance(base, Review)
