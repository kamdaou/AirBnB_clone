#!/usr/bin/python3
"""base_model - Contents our BaseModel"""
import datetime
import uuid
from dateutil import parser


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

    def __init__(self, *args, **kwargs):
        """initializes instances of BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs is not None:
            for key in kwargs:
                if key != '__class__':
                    setattr(self, key, kwargs[key])
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, parser.parse(kwargs[key]))
        else:
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
