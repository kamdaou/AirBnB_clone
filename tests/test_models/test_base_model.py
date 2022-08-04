#!/usr/bin/python3
"""
Tests for the base_model module
"""
import datetime
import unittest

from freezegun import freeze_time

from models.base_model import BaseModel


@freeze_time("2022-04-24")
class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel - Contains method that implement test cases
    Methods:
        test_create_instance: test if an instance of class BaseModel can be created
        test_dict: Test the to_dic method of BaseModel
    """

    def test_create_instance(self):
        """
        test if an instance of class BaseModel can be created
        and test its values.
        """
        my_base_model = BaseModel()
        my_second_base_model = BaseModel()
        self.assertIsInstance(my_base_model.created_at, datetime.datetime)
        self.assertIsInstance(my_base_model.updated_at, datetime.datetime)
        self.assertEqual(my_base_model.created_at, datetime.datetime(2022, 4, 24))
        self.assertEqual(my_base_model.updated_at, datetime.datetime(2022, 4, 24))
        self.assertNotEqual(my_base_model.id, my_second_base_model.id)

    def test_dict(self):
        """Test the to_dic method of BaseModel"""
        my_base_model = BaseModel()
        my_dic = my_base_model.to_dict()
        my_custom_dic = {
            'id': my_dic.get('id'),
            'created_at': datetime.datetime(2022, 4, 24).isoformat(),
            'updated_at': datetime.datetime(2022, 4, 24).isoformat(),
            '__class__': 'BaseModel',
        }
        self.assertEqual(my_dic, my_custom_dic)

    def test_dict_with_kwargs(self):
        """Test the to_dic method when a dictionary attribute is given"""
        my_base_model = BaseModel()
        my_base_model.test = 'test'
        my_dic = my_base_model.to_dict()
        my_second_base_model = BaseModel(**my_dic)
        my_custom_dic = {
            'id': my_dic.get('id'),
            'created_at': datetime.datetime(2022, 4, 24),
            'updated_at': datetime.datetime(2022, 4, 24),
            '__class__': 'BaseModel',
            'test': 'test'
        }
        self.assertIsInstance(my_second_base_model.updated_at, datetime.datetime)
        self.assertIsInstance(my_second_base_model.created_at, datetime.datetime)
        self.assertIsNot(my_base_model, my_second_base_model)
        self.assertEqual(my_second_base_model.to_dict(), my_custom_dic)