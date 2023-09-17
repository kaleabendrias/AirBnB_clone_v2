#!/usr/bin/python3

"""
an engine DBStorage
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from models.base_model import Base
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage():
    """
    a engine for the database; to save data to the database
    """
    __engine = None
    __session = None
    
    def __init__(self):
        """
        accepts the attr for the DBStorage
        """
        username = os.environ.get("HBNB_MYSQL_USER")
        passwd = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        database = os.environ.get("HBNB_MYSQL_DB")
        url = f"mysql+mysqldb://{username}:{passwd}@{host}/{database}"
        self.__engine = create_engine(url, pool_pre_ping=True)
        if  os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session all objects depending of the class name
        """
        objects = {}
        if cls is None:
            # if cls is None query all obj
            cls_list = [User, State, City, Amenity, Place, Review]
        else:
            cls_list = [cls]

        for cls in cls_list:
            query_result = self.__session.query(cls).all()
            for  obj in query_result:
                key =f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        return objects

    def new(self, obj):
        """
        adds new object to the database
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delets obj from the current session
        """
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        # recreate all tables in the database
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        # create a new session with scoped session factory
        self.__session.remove()
        self.__session = scoped_session(self.__session_factory)
