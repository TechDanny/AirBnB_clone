#!/usr/bin/python3
"""
define a city class That inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    create instances
    """
    state_id = ""
    name = ""
