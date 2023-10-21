#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)  # Password column
        first_name = Column(String(128))  # First name column (nullable)
        last_name = Column(String(128))  # Last name column (nullable)

        # Define the relationship with the Place class
        places = relationship(
                "Place",
                backref="user",
                cascade="all, delete-orphan"
                )

        # Define the relationship with the Review class
        reviews = relationship(
                "Review",
                backref="user",
                cascade="all, delete-orphan"
                )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""   
