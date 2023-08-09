#!/usr/bin/python3
"""
defines amenity that inherits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    create an instance
    """
    name = ""
