#!/usr/bin/python3
"""
Defines the class Amenity using Unittest
"""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class testAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_instance(self):
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
        self.assertIsInstance(my_amenity, BaseModel)

    def test_amenityFromBaseModel(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenityHasAttribute(self):
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertIsInstance(self.amenity.name, str)

    def test_amenityDefault(self):
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
