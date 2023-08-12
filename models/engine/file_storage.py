#!/usr/bin/python3

"""
    This module represents the storage system for
    this project. The storage method of choice here is
    serialization and deserialization of JSON(Javascript object Notation)
    objects
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
        This class represents a File storage class
    """

    __file_path = "file.json"  # file path to JSON file
    __objects = {}  # stores all dictionary objects by the class name id

    def all(self):
        """
            This public method returns the dictionary stored in
            '__objects' if any
        """
        return self.__objects

    def new(self, obj):
        """
            Add the objects to the __objects dictionary
            by using the objects id as the key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            This method serializes __objects dictionary
            to a JSON string and saves it to the
            file according to the file path
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            base_dic = {}
            for (key, value) in self.__objects.items():
                base_dic[key] = value.to_dict()

            file.write(json.dumps(base_dic))  # write json data to file

    def reload(self):
        """
            This method deserializes the JSON file to
            __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_string = file.read()  # get the json string
                original_dic = json.loads(json_string)
                # deserialize the json string to its original
                # structure

            """
                loop through the dictionary by getting key, value pairs
                and use the value to create a new object instance
                use the key as the key to store the new object in
                __objects
            """
            for key, value in original_dic.items():
                base_model = BaseModel(**value)
                self.__objects[key] = base_model
        except FileNotFoundError:
            pass
