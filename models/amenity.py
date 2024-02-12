#!/usr/bin/python3
"""Defines Amenity class"""
import sys
sys.path.append('/AirBnB_clone')
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""
    name = ""
