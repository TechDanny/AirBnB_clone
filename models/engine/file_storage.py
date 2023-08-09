#!/usr/bin/pythoni3
import locale
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

"""
This class serializes instances to a JSON file
and deserializes JSON file to instances
"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in objects in the dictionary
        """
        my_className = obj.__class__.__name__
        self.__objects[f"{my_className}.{obj.id}"] = obj

    def save(self):
        """
        serializes the object to JSON file
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w",
                  encoding=locale.getpreferredencoding()) as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file tp object if the path exists
        otherwise nothing happens
        """
        class_list = {"User": User,
                      "Place": Place,
                      "State": State,
                      "City": City,
                      "Amenity": Amenity,
                      "Review": Review
                      }
        try:
            with open(self.__file_path, "r",
                      encoding=locale.getpreferredencoding()) as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    my_className, obj_id = key.split(".")
                    self.__objects[key] = globals()[my_className](**value)
        except FileNotFoundError:
            pass
