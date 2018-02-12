#!/usr/bin/python3
"""
   This module contains the class definition for the Review object.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class definition for the Review model."""
    def __init__(self, *args, **kwargs):
        """Instantiates a Review object."""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(**kwargs)
