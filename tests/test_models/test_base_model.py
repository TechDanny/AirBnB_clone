#!/usr/bin/python3
"""
Defines a test model class
"""


import unittest
from models.base_model import BaseModel
import datetime
import uuid
import models
import os
import json


class TestBaseModel(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_is_default(self):
        n = self.value()
        self.assertEqual(type(n), self.value)

    def test_is_kwargs(self):
        n = self.value()
        dup = n.to_dict()
        new_model = BaseModel(**dup)
        self.assertFalse(new_model is n)

    def test_is_kwargs_int(self):
        n = self.value()
        dup = n.to_dict()
        dup.update({1: 2})
        with self.assertRaises(TypeError):
            new_model = BaseModel(**dup)

    def test_is_save(self):
        n = self.value()
        n.save()
        k = self.name + "." + n.id
        with open("file.json", "r") as fn:
            m = json.load(fn)
            self.assertEqual(m[k], n.to_dict())

    def test_is_str(self):
        n = self.value()
        self.assertEqual(str(n), "[{}] ({}) {}".format(self.name,
                         n.id, n.__dict__))

    def test_to_dict(self):
        n = self.value()
        m = n.to_dict()
        self.assertEqual(n.to_dict(), m)

    def test_kwargsIsNone(self):
        m = {None: None}
        with self.assertRaises(TypeError):
            new_model = self.value(**m)

    def test_kwargsIsOne(self):
        m = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new_model = self.value(**m)

    def test_is_id(self):
        n = self.value()
        self.assertEqual(type(n.id), str)

    def test_with_created_at(self):
        n = self.value()
        self.assertEqual(type(n.created_at), datetime.datetime)

    def test_with_updated_at(self):
        n = self.value()
        self.assertEqual(type(n.updated_at), datetime.datetime)
        m = n.to_dict()
        n = BaseModel(**m)
        self.assertFalse(n.created_at == n.updated_at)


if __name__ == "__main__":
    unittest.main()
