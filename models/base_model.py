#!/usr/bin/python3
"""This module contains the BaseModel class."""
from datetime import datetime
import uuid
import models
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
    summary line.

    This class will define all common.
    attributes/methods for other classes.
    Attributes:
        id: primary key, string of 60 characters, unique, can’t be null
        created_at: datetime, can’t be null, default = current datetime
        updated_at: datetime, can’t be null, default = current datetime
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """__init__ constructor method for BaseModel class."""
        if kwargs != {}:  # if kwargs is not empty
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # models.storage.new(self) - moved to save method
        if not self.id:
            self.id = str(uuid.uuid4())
        d = datetime.now()
        if not self.created_at:
            self.created_at = d
            self.updated_at = d
        if not self.updated_at:
            self.updated_at = d

    def __str__(self):
        """__str__ method to print a string representation of the class."""
        classname = self.__class__.__name__
        return ("[{}] ({}) {}".format(classname, self.id, self.__dict__))

    def save(self):
        """Save method to update the public instance attribute updated_at."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """to_dict method to return a dictionary containing all keys/values."""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """Delete method to delete the current instance from the storage."""
        models.storage.delete(self)
