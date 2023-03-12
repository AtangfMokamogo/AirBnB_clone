#!/usr/bin/python3
"""implements the city module"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """Represents the City our user is in

    Attributes:
        state_id (str): the uuid of the state the city is located in
        name (str): the name of the city instance
    """
    state_id = ""
    name = ""
