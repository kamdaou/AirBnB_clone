#!/usr/bin/python3
"""tests for the file storage"""
import json
import unittest

from constants import FILE_NAME
from models import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage - Test the file storage class
    Methods:
        test_save_data: Test if a saved data can be written in the json file
    """

    def test_save_data(self):
        """Test if a saved data can be written in the json file"""
        my_model = BaseModel()
        my_dic = my_model.to_dict()
        my_model.save()
        my_custom_dic = {
            'id': my_dic.get('id'),
            'created_at': my_dic['created_at'],
            'updated_at': my_dic['updated_at'],
            '__class__': 'BaseModel',
        }
        with open(FILE_NAME, "r") as fp:
            my_json_dict = json.load(fp)
            self.assertEqual(
                my_json_dict['BaseModel.' + my_dic.get('id')]['id'],
                my_custom_dic.get('id')
            )
            self.assertEqual(
                my_json_dict['BaseModel.' + my_dic.get('id')]['created_at'],
                my_custom_dic.get('created_at')
            )
            self.assertEqual(
                my_json_dict['BaseModel.' + my_dic.get('id')]['__class__'],
                my_custom_dic.get('__class__')
            )
