#!/usr/bin/python3
"""base_model - Contents our BaseModel"""
import uuid
from datetime import datetime

import models


class BaseModel:
    """
    BaseModel - defines all common attributes/methods for other classes

    Attributes:
        id (str): id of the instance.
        created_at (datetime): time when the instance has been created.
        updated_at (datetime): time when the instance has been updated.

    Methods:
         save: updates the public instance attribute
          updated_at with the current datetime.
         to_dict: returns a dictionary containing
          all keys/values of __dict__ of the instance.
    """

    def __str__(self):
        """prints class name, id and dict"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def __init__(self, *args, **kwargs):
        """initializes instances of BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs != {}:
            for key in kwargs:
                if key != '__class__':
                    setattr(self, key, kwargs[key])
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute
         updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        Returns:
            a dictionary
        """
        cust_dic = dict()
        for key in iter(self.__dict__):
            value = self.__dict__[key]
            if value is not None:
                if hasattr(value, 'isoformat'):
                    cust_dic[key] = value.isoformat()
                else:
                    if hasattr(value, 'to_dict'):
                        cust_dic[key] = value.to_dict()
                    else:
                        cust_dic[key] = value
        cust_dic['__class__'] = self.__class__.__name__
        return cust_dic
