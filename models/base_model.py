#!/usr/bin/python3
"""Defines BaseModel class"""
import sys
sys.path.append('/AirBnB_clone')
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class"""
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    date_format = '%Y-%m-%dT%H:%M:%S.%f'
                    parsed_date = datetime.strptime(value, date_format)
                    setattr(self, key, parsed_date)
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
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update public instance attribute updated_at with current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary containing all values of __dict__ of instance"""

        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
