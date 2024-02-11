#!/usr/bin/python3
"""
module creates a User class
defines a city class
"""
from base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ""
    name = ""
