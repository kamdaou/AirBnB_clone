#!/usr/bin/python3
"""test for city class"""
import unittest
from datetime import datetime

from models.city import City


class TestCity(unittest.TestCase):
    """
    TestCity: Create tests for city class
    Methods:
        test_create_city: Test if an instance of city can be created
    """
    def test_create_city(self):
        """Test if an instance of city can be created"""
        my_base_model = City()
        my_second_base_model = City()
        self.assertIsInstance(my_base_model.created_at, datetime)
        self.assertIsInstance(my_base_model.updated_at, datetime)
        self.assertNotEqual(my_base_model, my_second_base_model)
        self.assertEqual(my_base_model.to_dict().get('__class__'), "City")
