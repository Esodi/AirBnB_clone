#!/usr/bin/phython3
"""serializes instances to a JSON file and deserializes JSON file to instances

"""


import json
import os
import importlib.util


class FileStorage:
    '''class that convert to json'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns __objects dict'''
        return self.__objects

    def new(self, obj):
        '''add an object to __object dict'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''saves to json string'''
        serialized_objs = {}
        for key, value in FileStorage.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module_name = self.get_module_name(class_name)
                    module_path = os.path.join("models", module_name + ".py")
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    class_ = getattr(module, class_name)
                    obj = class_(**value)
                    setattr(obj, "__class__", class_)  # Set the class dynamically
                    self.__objects[key] = obj

    def get_module_name(self, class_name):
        if class_name == 'BaseModel':
            return 'base_model'
        else:
            return class_name.lower()

