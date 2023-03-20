#!/usr/bin/python3
"""implements the state module"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents the state where user is located

    Attributes:
        name (str): the name of the state
    """
    name = ""
