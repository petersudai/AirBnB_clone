#!/usr/bin/python3
"""This module creates a User class, Defines the User class."""
import sys
sys.path.append('/AirBnB_clone')
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
