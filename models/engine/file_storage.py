#!/usr/bin/python3
"""
defines the file storage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """ defines an abstracted file storage engine
        Attributes:
            __file_path (str): path to JSON file
            __objects (dict): will store objects by class.id
    """

    __file_path = "file.json"

    # using this dictionary, we will store objects using id
    __objects = {}

    def all(self):
        """ returns copy of __objects when called """
        return self.__objects

    def new(self, obj):
        """
        stores obj in __objects dictionary using
            key = <obj class name>.id,
            value = obj.to_dict()


            Args:
                obj (:obj: `BaseModel`): object to add to __objects
        """
        # Generate key here
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            json.dump({k: v.to_dict()
                       for k, v in self.__objects.items()}, f, indent=4)

    def reload(self):
        """Deserialize JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, mode="r") as f:
                data = json.load(f)
                for key, value in data.items():
                    #
                    class_name = key.split('.')[0]
                    cls = globals()[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
