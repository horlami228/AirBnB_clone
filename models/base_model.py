#!/usr/bin/python3
# Make it a python script
from uuid import uuid4
# import the uuid module for the id
import datetime
# import module to show the date and time for instances created

"""
This module defines a class BaseModel where all other classes will
inherit from
"""


class BaseModel:
    """
        Defining a class BaseModel
    """

    def __init__(self):
        """
        Initialize a new instance object of
        the BaseModel
        """
    # public attribute that contains uuid for every instance of the class
        self.id = str(uuid4())

    # public attribute for the datetime creation of the object
        self.created_at = datetime.datetime.utcnow()

    # public attribute for updated creation time
        self.updated_at = datetime.datetime.utcnow()

    def __str__(self):
        """
        This magic method returns a string representation
        of the BaseModel class
        """

        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """
            This public method updates the updated_at attribute
            with the updated date and time
        """
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        """
            This public method returns a new dictionary containing the
            keys and values from the __dict__ which is a special attribute
        """

        dic = self.__dict__.copy()  # made a copy of the object dictionary
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()

        return dic
