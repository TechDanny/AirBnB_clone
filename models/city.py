#!/usr/bin/python3
"""
Define a City class that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    create instances
    """
    state_id = ""
    name = ""
