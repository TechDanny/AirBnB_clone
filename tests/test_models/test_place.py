#!/usr/bin/python3
"""
Defines a Place unittest
"""


import unittest
from models.place import Place


class testPlace(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        n = self.value()
        self.assertEqual(type(n.city_id), str)

    def test_userId(self):
        n = self.value()
        self.assertEqual(type(n.user_id), str)

    def test_name(self):
        n = self.value()
        self.assertEqual(type(n.name), str)

    def test_description(self):
        n = self.value()
        self.assertEqual(type(n.description), str)

    def test_numberRooms(self):
        n = self.value()
        self.assertEqual(type(n.number_rooms), int)

    def test_numberBathrooms(self):
        n = self.value()
        self.assertEqual(type(n.number_bathrooms), int)

    def test_maxGuest(self):
        n = self.value()
        self.assertEqual(type(n.max_guest), int)

    def test_priceByNight(self):
        n = self.value()
        self.assertEqual(type(n.price_by_night), int)

    def test_latitude(self):
        n = self.value()
        self.assertEqual(type(n.latitude), float)

    def test_longitude(self):
        n = self.value()
        self.assertEqual(type(n.longitude), float)

    def test_amenity_ids(self):
        n = self.value()
        self.assertEqual(type(n.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
