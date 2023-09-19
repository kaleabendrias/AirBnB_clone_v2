#!/usr/bin/python3

""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    storageType = os.environ.get("HBNB_TYPE_STORAGE")

    if storageType == "db":
        name = Column(String(28), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=True)
        state = relationship("State")
        places = relationship(
                "Place",
                backref="cities",
                cascade="all, delete-orphan"
                )
    else:
        name = ""
        state_id = ""
