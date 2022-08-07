#!/usr/bin/python3
"""test for amenity class"""
import unittest
from datetime import datetime

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    TestAmenity: Create tests for amenity class
    Methods:
        test_create_amenity: Test if an instance of amenity can be created
    """
    def test_create_amenity(self):
        """Test if an instance of amenity can be created"""
        my_base_model = Amenity()
        my_second_base_model = Amenity()
        self.assertIsInstance(my_base_model.created_at, datetime)
        self.assertIsInstance(my_base_model.updated_at, datetime)
        self.assertNotEqual(my_base_model, my_second_base_model)
        self.assertEqual(my_base_model.to_dict().get('__class__'), "Amenity")
