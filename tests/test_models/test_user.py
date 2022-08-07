#!/usr/bin/python3
"""test for user class"""
import unittest
from datetime import datetime

from models.user import User


class TestUser(unittest.TestCase):
    """
    TestUser: Create tests for user class
    Methods:
        test_create_user: Test if an instance of user can be created
    """
    def test_create_user(self):
        """Test if an instance of user can be created"""
        my_base_model = User()
        my_second_base_model = User()
        self.assertIsInstance(my_base_model.created_at, datetime)
        self.assertIsInstance(my_base_model.updated_at, datetime)
        self.assertNotEqual(my_base_model, my_second_base_model)
        self.assertEqual(my_base_model.to_dict().get('__class__'), "User")
