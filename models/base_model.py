#!/usr/bin/python3
"""base_model - Contents our BaseModel"""
import datetime
import uuid


class BaseModel:
    """
    BaseModel - defines all common attributes/methods for other classes

    Attributes:
        id (str): id of the instance.
        created_at (datetime.datetime): time when the instance has been created.
        updated_at (datetime.datetime): time when the instance has been updated.

    Methods:
         save: updates the public instance attribute updated_at with the current datetime.
         to_dict: returns a dictionary containing all keys/values of __dict__ of the instance.
    """

    def __str__(self):
        """prints class name, id and dict"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def __init__(self):
        """initializes instances of BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        Returns:
            a dictionary
        """
        my_dict = self.__dict__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
