#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribuute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""

        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
