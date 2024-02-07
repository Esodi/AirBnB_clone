#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods for other classes

"""


import uuid
import datetime

class BaseModel:
    """Base class for all coming subclasses"""

    def __init__(self, my_num=None, name=None):
        '''initialize instance attributes'''
        self.my_number = my_num
        self.name = name
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

    def save(self):
        '''updates time of an instance'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''Return dictionary form of object's attributes'''
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__

    def __str__(self):
        '''Returns the string form of an object'''
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"
