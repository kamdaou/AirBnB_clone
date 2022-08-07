#!/usr/bin/python3
"""contains Place class"""
from models import BaseModel


class Place(BaseModel):
    """Place class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guess = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    amenity_ids = list()
