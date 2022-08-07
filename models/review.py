#!/usr/bin/python3
"""contains Review class"""
from models import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""
