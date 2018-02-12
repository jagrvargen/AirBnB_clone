#!/usr/bin/python3
"""
Unit tests for state
"""
import unittest
import json
import sys
import io
import uuid
import datetime
from models.state import State


class TestState(unittest.TestCase):
    """This class contains unit tests for the State class."""

    def test_is_instance(self):
        """Set up an instance of a State."""
        base = State()
        self.assertIsInstance(base, State)
