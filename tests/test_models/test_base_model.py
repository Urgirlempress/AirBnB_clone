#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""


import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case for base model class"""

    def setUp(self):
        """Sets the test methods up"""
        pass

    def tearDown(self):
        """Tear down test methods"""
        pass

    def test_instantiation(self):
        """Test for the instantiation of the base class"""

        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

