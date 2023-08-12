#!/usr/bin/python3
"""
import all useful models
"""
import uuid
from datetime import datetime
import models

"""
Defining all common attributes/methods for
other classes in BaseModel
"""


class BaseModel:
    """
    create instances
    """
    def __init__(self, *args, **kwargs):
        """
        arguments for constructor of base model
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        prints class.name, self.id, self.__dict__
        """
        my_className = self.__class__.__name__
        return "[{}] ({}) {}".format(my_className, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys and values
        """
        rslt = self.__dict__.copy()
        rslt['created_at'] = self.created_at.isoformat()
        rslt['updated_at'] = self.updated_at.isoformat()
        rslt['__class__'] = self.__class__.__name__
        return rslt
