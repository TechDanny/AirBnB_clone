#!/usr/bin/python3
"""
Defines  a class test_file_storage
"""


import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class test_file_storage(unittest.TestCase):
    """
    create the methods
    """
    def setUp(self):
        """
        first set up
        """
        empty_list = []
        for k in storage.FileStorage._FileStorage__object.keys():
            empty_list.append(k)
        for k in empty_list:
            del storage.FileStorage._FileStorage__objects[k]

    def tearDown(self):
        """
        removes json
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_obj_is_empty(self):
        """
        checks if object is empty
        """
        self.assertEqual(len(storage.all()), 0)

    def test_is_new(self):
        """
        checks if is new
        """
        new_model = BaseModel()
        for b in storage.all().values():
            x = b
        self.assertTrue(x is b)

    def testAll(self):
        """
        tests for all
        """
        new_model = BaseModel()
        x = storage.all()
        self.assertIsInstance(x, dict)

    def test_base_model_is_instance(self):
        """
        checks if base model is instance
        """
        new_model = BaseModel()
        self.assertFalse(os.path.exists("file.json"))

    def test_is_empty(self):
        """
        checks if obj is empty
        """
        new_model = BaseModel()
        x = new_model.to_dict()
        new_model.save()
        dup = BaseModel(**x)
        self.assertNotEqual(os.path.getsize("file.json"), 0)

    def test_is_saved(self):
        """
        saves the updated
        """
        new_model = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_is_reload(self):
        """
        checks if it is a reload
        """
        new_model = BaseModel()
        storage.save()
        storage.reload()
        for k in storage.all().values():
            new_load = k
        self.assertEqual(new_model.to_dict()["id"], new_loaded.to_dict()["id"])

    def test_base_model_is_save(self):
        """
        checks if base model is saved
        """
        new_model = BaseModel()
        new_model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_typePath(self):
        """
        checks the type of path
        """
        self.assertEqual(type(storage.FileStorage.__file_path), str)

    def test_type_obj(self):
        """
        checks the type of object
        """
        self.assertEqual(type(storage.all()), dict)

    def test_formatKey(self):
        """
        checks the format key
        """
        new_model = BaseModel()
        my_id = new_model.to_dict()["id"]
        for k in storage.all().keys():
            m = k
        self.assertEqual(m, "BaseModel" + "." + my_id)

    def test_StorageCreated(self):
        """
        checks if storage is created
        """
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
