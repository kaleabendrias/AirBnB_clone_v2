#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        from models import storage
        if not kwargs:
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)  # Moved from __init__
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        from models import storage
        """Deletes the current instance from storage"""
        storage.delete(self)
