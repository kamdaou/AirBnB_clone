#!/usr/bin/python3
"""contains user class"""
from models import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
