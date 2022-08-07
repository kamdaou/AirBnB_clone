#!/usr/bin/python3
"""test for state class"""
import unittest
from datetime import datetime

from models.state import State


class TestState(unittest.TestCase):
    """
    TestState: Create tests for state class
    Methods:
        test_create_state: Test if an instance of state can be created
    """
    def test_create_state(self):
        """Test if an instance of state can be created"""
        my_base_model = State()
        my_second_base_model = State()
        self.assertIsInstance(my_base_model.created_at, datetime)
        self.assertIsInstance(my_base_model.updated_at, datetime)
        self.assertNotEqual(my_base_model, my_second_base_model)
        self.assertEqual(my_base_model.to_dict().get('__class__'), "State")
