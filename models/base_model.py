#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods for other classes

"""


import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    """Base class for all coming subclasses"""

    def __init__(self, *args, **kwargs):
        '''init method for BaseModel class'''
        if kwargs:
            for key, value in kwargs.items():
                if 'created_at' in kwargs and isinstance(kwargs['created_at'], str):
                    kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
                if 'updated_at' in kwargs and isinstance(kwargs['updated_at'], str):
                    kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:     
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
        storage.new(self)

    def save(self):
        '''updates time of an instance'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Return dictionary form of object's attributes'''
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__

    def __str__(self):
        '''Returns the string form of an object'''
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"
