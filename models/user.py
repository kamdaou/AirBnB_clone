#!/usr/bin/python3
"""contains user class"""
from models import BaseModel


class User(BaseModel):
    """user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
