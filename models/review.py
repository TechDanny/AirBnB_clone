#!/usr/bin/python3
"""
Defines a class Review that inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    instances
    """
    place_id = ""
    user_id = ""
    text = ""
