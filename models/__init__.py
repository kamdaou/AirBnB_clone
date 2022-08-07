#!/usr/bin/python3
"""__init__ - create a unique FileStorage instance for the application"""
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
