#!/usr/bin/python3
"""
    This module is for testing the BaseModel
    unittest classes:
        TestBaseModelId - line 12

"""
import unittest
from models.base_model import BaseModel
import os


class TestBaseModelId(unittest.TestCase):
    """
        This test class is to test the
        ID assignment
    """

    def test_with_id(self):
        """
            get id of the BaseModel object instance
        """
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        self.assertEqual(model1.id, model1.id)
        self.assertEqual(model2.id, model2.id)
        self.assertEqual(model3.id, model3.id)

    def test_id_not_the_same(self):
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        self.assertNotEqual(model2.id, model1.id)
        self.assertNotEqual(model3.id, model2.id)
        self.assertNotEqual(model1.id, model3.id)


if __name__ == '__main__':
    unittest.main()
