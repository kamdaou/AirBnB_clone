#!/usr/bin/python3
"""test for review class"""
import unittest
from datetime import datetime

from models.review import Review


class TestReview(unittest.TestCase):
    """
    TestReview: Create tests for review class
    Methods:
        test_create_review: Test if an instance of review can be created
    """
    def test_create_review(self):
        """Test if an instance of review can be created"""
        my_base_model = Review()
        my_second_base_model = Review()
        self.assertIsInstance(my_base_model.created_at, datetime)
        self.assertIsInstance(my_base_model.updated_at, datetime)
        self.assertNotEqual(my_base_model, my_second_base_model)
        self.assertEqual(my_base_model.to_dict().get('__class__'), "Review")
