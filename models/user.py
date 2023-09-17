#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'  # Table name
    email = Column(String(128), nullable=False)  # Email column (not null)
    password = Column(String(128), nullable=False)  # Password column (not null)
    first_name = Column(String(128))  # First name column (nullable)
    last_name = Column(String(128))  # Last name column (nullable)
