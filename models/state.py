#!/usr/bin/python3
"""
module creates a User class
Defines State class
"""
import sys
sys.path.append('/AirBnB_clone')
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    name = ""
