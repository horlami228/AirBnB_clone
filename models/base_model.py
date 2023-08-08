#!/usr/bin/python3
# Make it a python script
from uuid import uuid4 # import the uuid module for the id
import datetime # import module to show the date and time for instances created
"""
	This module defines a class BaseModel where all other classes will
	inherit from
""" 

class BaseModel():
	"""
		Defining a class BaseModel
	"""
	def __init__(self):
		"""
			Initialize a new instance object of 
			the BaseModel
		"""
		# public instance attribute that contains uuid for every instance of the class
		self.id = str(uuid4())
		
		# public instance attribute for the date and time an instance of this class was created
		self.created_at =  datetime.datetime.now()
		
		# public instance attribute for the date and time the object instance was updated
		self.updated_at =  datetime.datetime.now()

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
		self.updated_at = datetime.datetime.now