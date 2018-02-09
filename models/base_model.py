#!/usr/bin/python3
"""
base_model
"""
import uuid
from datetime import datetime

class BaseModel():
    """
       This is the class definition of the Base Model from which all objects in
       the AirBnB clone will inherit.
    """
    def __init__(self, *args, **kwargs):
        """__init__ for base_model object"""
        id_temp = uuid.uuid4()
        id_str = id_temp.urn
        self.id = id_str[9:]
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of base_model object"""
        pass
