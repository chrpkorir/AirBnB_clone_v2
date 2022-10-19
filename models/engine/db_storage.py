#!/usr/bin/python3
""" The AirBnB engine."""
from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from model.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage():
    __engine = None
    __session = None
    dialect = 'mysql'
    driver = 'mysqldb'

    def __init__(self):
        self.__engine = create_engine("{}+{}://{}@{}/{}".
                                      format(self.dialect, self.driver,
                                          getenv('HBNB_MYSQL_USER'),
                                          getenv('HBNB_MYSQL_PWD'),
                                          getenv('HBNB_MYSQL_HOST'),
                                          getenv('HBNB_MYSQL_DB'),
                                          pool_pre_ping=True))
        self.__session = sessionmaker(bind=self.__engine)
        session = self.__session()
        if getenv('HBNB_ENV') == 'test':
            data = session.query().all()
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """ this method returns a dictionary """
        my_dict = {}
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(obj.name, obj.id)
                my_dict[key] = obj
        else:
            for obj in self.__session.query(classes).all():
                key = "{}.{}".format(obj.name, obj.id)
                my_dict[key] = obj
        return my_dict
    
    def new(self, obj):
        """ add the object to the current database session """
        if obj:
            self.__session.add(obj)
    
    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the objects from the database """
        if obj:
            stored_obj = self.__session.query(obj).get(obj.id)
            self.__session.delete(stored_obj)
    
    def reload(self):
        """ reloads a table from the database """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
