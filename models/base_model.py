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
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary from a BaseModel instance."""
        attr_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == self.created_at or key == self.updated_at:
                key.isoformat()
            attr_dict[key] = value
        return attr_dict
