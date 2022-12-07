#!/usr/bin/python3
"""This Module contains the DBStorage engine."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import environ as env


class DBStorage():
    """DBStorage class."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage class."""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                env['HBNB_MYSQL_USER'],
                env['HBNB_MYSQL_PWD'],
                env['HBNB_MYSQL_HOST'],
                env['HBNB_MYSQL_DB']
            ), pool_pre_ping=True
        )
        if env.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
