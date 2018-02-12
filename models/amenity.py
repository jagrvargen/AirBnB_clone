#!/usr/bin/python3
"""
   This module contains the class definition for the Amenity object.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the class definition for the Amenity object."""
    def __init__(self, *args, **kwargs):
        """Instantiates an Amenity object."""
        self.name = ""
        super().__init__(**kwargs)
