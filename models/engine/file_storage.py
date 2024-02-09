#!/usr/bin/python3
import json
from os import path


class FileStorage:
    """
    class that serializes instances to JSON file and deserializes
    JSON file to instances
    """

    __file_Path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(self.__file_path, 'w') as file:
            data = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(',')
                    module_name = 'models.' + call_name
                    module = __import__(module_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    self.__objects[key] = class_(**value)
