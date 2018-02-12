#!/usr/bin/python3
"""
   This module contains the class definition for the State object which inherits
   from the BaseModel class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is the class definition for a State object."""
    def __init__(self, *args, **kwargs):
        """Instantiates a state object."""
        self.name = ""
        super().__init__(**kwargs)
