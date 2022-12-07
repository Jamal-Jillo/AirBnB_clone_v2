#!/usr/bin/python3
"""Class FileStorage."""
import json
from os.path import exists
from textwrap import indent
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Class FileStorage."""

    __file_path = "file.json"
    __objects = {}  # Empty Dictionary

    def all(self, cls=None):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        # This one works too:
        # if obj is not None:
        # key = obj.__class__.__name__ + "." + obj.id
        # self.__objects[key] = obj
        self.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        odict = self.__objects
        data = {obj: odict[obj].to_dict() for obj in odict.keys()}
        # for key in self.__objects:
        #    data[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    def reload(self):
        """
        Summary line.

        Deserialize the JSON file to __objects(only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised).
        """
        # if exists(self.__file_path):
        #    with open(self.__file_path, 'r') as jsonfile:
        #        data = json.load(jsonfile)
        #        for key in data:
        #            self.__objects[key] =\
        #                eval(data[key]["__class__"])(**data[key])

        #  Both of these work:
        try:
            with open(self.__file_path) as f:
                data = json.load(f)
                for o in data.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside."""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()
