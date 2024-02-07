#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods for other classes

"""
import uuid
import datetime

class BaseModel:
    """Base class for all coming subclasses"""

    def __init__(self, *args, **kwargs):     

        if kwargs:
            for key, value in kwargs.items():
                 if key == 'created_at' or key == 'updated_at':
                     value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                 elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.datetime.now()
            if 'updated_at' not in kwargs:     
                self.updated_at = datetime.datetime.now()

            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

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
