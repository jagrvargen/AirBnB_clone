#!/usr/bin/python3
"""
   This module contains the class definition for the User object which inherits
   from the BaseModel class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class definition for a User object."""
    def __init__(self, *args, **kwargs):
        """Instantiates a User object."""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(self)
