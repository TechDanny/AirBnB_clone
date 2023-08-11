#!/usr/bin/python3

"""
Defining the unit test for the class City
"""

import unittest
from models.city import City


class testCity(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_city_id(self):
        m = self.value()
        self.assertEqual(type(m.state_id), str)

    def testName(self):
        m = self.value()
        self.assertEqual(type(m.name), str)


if __name__ == "__main__":
    unittest.main()
