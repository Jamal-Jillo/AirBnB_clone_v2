#!/usr/bin/python3
"""City Module for AirBnB project."""
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
# from models import storage
# from models.city import City


class City(BaseModel, Base):
    """City class that describes a city.

    Attributes:
        state_id (str): The state id. It will be the State.id
        name (str): The city name
        __tablename__ (str): The name of the MySQL table to store Cities
    """

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = 'cities'
    cities = relationship('City', backref='state', cascade='all, delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City.

            instances with state_id equals to the current State.id
            """
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
