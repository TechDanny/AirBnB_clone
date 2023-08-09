#!/usr/bin/python3
"""
defines a class Review that inheritsfrom BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    instances
    """
    place_id = ""
    user_id = ""
    text = ""
