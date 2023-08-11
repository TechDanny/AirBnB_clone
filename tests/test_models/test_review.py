#!/usr/bin/python3
"""
Defining the class Review using unittest
"""


import unittest
from models.review import Review


class testReview(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_placeId(self):
        m = self.value()
        self.assertEqual(type(m.place_id), str)

    def test_userId(self):
        m = self.value()
        self.assertEqual(type(m.user_id), str)

    def test_text(self):
        m = self.value()
        self.assertEqual(type(m.text), str)


if __name__ == "__main__":
    unittest.main()
