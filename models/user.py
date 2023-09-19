#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'  # Table name
    storageType = os.environ.get("HBNB_TYPE_STORAGE")

    if storageType == "db":
        email = Column(String(128), nullable=False)  # Email column (not null)
        password = Column(String(128), nullable=False)  # Password column (not null)
        first_name = Column(String(128))  # First name column (nullable)
        last_name = Column(String(128))  # Last name column (nullable)

        places = relationship(
                "Place",
                backref="user",
                cascade="all, delete-orphan"
                )
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
