#!/usr/bin/python3
"""
   This mnodule contains the class definition for the Place object.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This is the class definition for the Place object."""
    def __init__(self, *args, **kwargs):
        """Instantiates a Place object."""
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(**kwargs)
