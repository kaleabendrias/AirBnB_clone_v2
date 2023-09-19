#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    storageType = os.environ.get("HBNB_STORAGE_TYPE")

    if storageType == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""

    if storageType  == "db":
        cities = relationship(
                "City",
                backref="state",
                cascade="all, delete-orphan"
                )
    else:
        @property
        def cities(self):
            """
            getter attr that returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            city_objs = storage.all("City").values()
            return [city for city in city_objs if city.state_id == self.id]
