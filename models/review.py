#!/usr/bin/python3
"""Implements reviews module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the Reviews class

    Attributes:
        place_id (str): represents the id of the place
        user_id (str): the id of the user
        text (str): the review
    """

    place_id = ""
    user_id = ""
    text = ""
