#!/usr/bin/python3
"""the module which handles review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """the class which handles reviews"""
    place_id = ""
    user_id = ""
    text = ""
