#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    storage_type = os.environ.get("HBNB_TYPE_STORAGE")
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        place_amenity = Table(
                'place_amenity',
                Base.metadata,
                Column(
                    "place_id",
                    String(60),
                    ForeignKey("places.id"),
                    primary_key=True,
                    nullable=False
                    ),
                Column(
                    'amenity_id',
                    String(60),
                    ForeignKey('amenities.id'),
                    primary_key=True,
                    nullable=False
                    )
                )
        reviews = relationship(
                "Review",
                backref="place",
                cascade="all, delete-orphan"
                )
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ a review getter method """
            from models import storage
            return [review for review in storage.all(Review).values() if review.place_id == self.id]

        @property
        def amenities(self):
            """
            getter attr for amenities in FileStorage
            """
            from models import storage
            amenities_list = []
            for amenity_id  in self.amenity_ids:
                amenity = storage.get(Amenity, amenity_id)
                if amenity:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attr for amenities in file storage
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
