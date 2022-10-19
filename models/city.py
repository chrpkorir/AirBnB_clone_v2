#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from  sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('stated.id'), nulllable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
