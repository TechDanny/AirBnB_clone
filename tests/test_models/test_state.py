#!/usr/bin/python3
"""
Defines the class State by the help of unittest
"""


import unittest
from models.state import State


class testState(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        m = self.value()
        self.assertEqual(type(m.name), str)


if __name__ == "__main__":
    unittest.main()
