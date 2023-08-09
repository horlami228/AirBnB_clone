#!/usr/bin/python3
"""
    This module defines a class BaseModel where all other classes will
    inherit from
"""
from uuid import uuid4
# import the uuid module for the id
import datetime
# import module to show the date and time for instances created
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"  # formatted date and time


class BaseModel:
    """
        Defining a class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance object of
        the BaseModel

        Args:
            *args(positional arg): Positional argument
            **kwargs(keyword arg): key value pair arguments
        """

        """
            looping through the keyword argument
            for the purpose of initializing a new instance with
            it
        """
        if kwargs:
            for (key, value) in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    # convert date string to datetime object
                    date_string = value
                    print("date_string:", date_string)
                    date_object = datetime.datetime.strptime(date_string,
                                                             DATE_FORMAT)

                    # strptime() to convert to object
                    value = date_object
                    print("date_object:", date_object)
                    setattr(self, key, value)
                    # set the created_at or updated_at attributes
                setattr(self, key, value)
                # set every other passed argument
        else:
            # public attribute that contains uuid
            # for every instance of the class
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

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

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
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()

        return dic
