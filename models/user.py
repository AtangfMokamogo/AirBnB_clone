#!/usr/bin/python3
"""Defines a User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in our AirBnB

    Attributes:
        email (str): Represents users emails
        password (str): Users passwords
        first_name (str): Users first names
        last_name (str): Users last names
    """

    email = ""
    password = ""
    fist_name = ""
    last_name = ""
