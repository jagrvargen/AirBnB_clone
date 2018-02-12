#!/usr/bin/python3
"""
   This module contains the class definition for the City object which inherits
   from the BaseModel class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This is the class definition for a City object."""
    def __init__(self, *args, **kwargs):
        """Instantiates a city object."""
        self.state_id = ""
        self.name = ""
        super().__init__(**kwargs)
