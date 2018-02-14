#!/usr/bin/python3
"""
   This module contains the class definition for the Review object.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class definition for the Review model."""
    place_id = ""
    user_id = ""
    text = ""
