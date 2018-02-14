#!/usr/bin/python3
"""
   This module contains the class definition for the User object which inherits
   from the BaseModel class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class definition for a User object."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
