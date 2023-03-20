#!/usr/bin/python3
"""Implements the place module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the place class

    Attribute:
        city_id (str): the id of the city
        user_id (str): the iser id
        name (str): the name of the place
        description (str): place description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): number of allowed guests
        price_by_night (int): price per night of the place
        latitude (float): the latitude coordinate of the place
        longitude (float): longitude coordinate of the place
        amenity_id (str): []
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
