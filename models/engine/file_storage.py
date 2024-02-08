#!/usr/bin/phython3
"""serializes instances to a JSON file and deserializes JSON file to instances

"""


import json
import os

class FileStorage:
    '''class that convert to json'''

    def __init__(self, *args, **kwargs):
        '''initialiazation method'''
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        '''returns __objects dict'''
        return self.__objects

    def new(self, obj):
        '''add an object to __object dict'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''saves to json string'''
        with open(self.__file_path, 'w') as json_f:
            json.dump(self.__objects, json_f, indent=4)

    def reload(self):
        '''loads from json string'''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_f:
              self.__objects = json.load(json_f)
