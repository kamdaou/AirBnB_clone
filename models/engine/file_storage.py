#!/usr/bin/python3
"""file_storage - contains FileStorage class"""
import json
import models
from constants import FILE_NAME


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances:
    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store
        all objects by <class name>.id
        (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)
    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to
        __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
    """
    __file_path = FILE_NAME
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[str(obj.__class__.__name__) + '.' + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w+') as fp:
            dic = {}
            for key in iter(self.__objects):
                value = self.__objects[key]
                dic[key] = value.to_dict()
            json.dump(dic, fp)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as fp:
                dic = json.load(fp)
                for key in iter(dic):
                    self.__objects[key] = models.BaseModel(dic[key])
        except FileNotFoundError:
            pass
