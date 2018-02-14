#!/usr/bin/python3
"""
   This module contains the class definition for the City object which inherits
   from the BaseModel class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This is the class definition for a City object."""
    state_id = ""
    name = ""
