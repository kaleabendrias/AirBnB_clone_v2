#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
import os

class Amenity(BaseModel, Base):
    """ this is a table amenity or the class amenity """
    __tablename__ = "amenities"

    storageType = os.environ.get("HBNB_TYPE_STORAGE")

    if storageType == "db":
        name = Column(String(128), nullable=False)
        
        place_amenities  = relationship(
                "Place",
                secondary="place_amenity",
                viewonly=False,
                back_populates="amenities"
                )
    else:
        name = ""
