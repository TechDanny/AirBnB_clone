#!/usr/bin/python3
"""
defines the class State unittest
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
