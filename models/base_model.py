import uuid
from datetime import datetime

"""
Defines all common attributes/methods for
other classes
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        my_className = self.__class__.__name__
        return "[{}] ({}) {}".format(my_className, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        rslt = self.__dict__.copy()
        rslt['__class__'] = self.__class__.__name__
        rslt['created_at'] = self.created_at.isoformat()
        rslt['updated_at'] = self.updated_at.isoformat()
        return rslt
