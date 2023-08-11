#!/usr/bin/python3

"""
Test class of the user
"""


import unittest
from models.user import User


class Test_user(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def testFirstName(self):
        n = self.value()
        self.assertEqual(type(n.first_name), str)

    def testLastName(self):
        n = self.value()
        self.assertEqual(type(n.last_name), str)

    def testEmail(self):
        n = self.value()
        self.assertEqual(type(n.email), str)

    def testPassword(self):
        n = self.value()
        self.assertEqual(type(n.password), str)


if __name__ == "__main__":
    unittest.main()
