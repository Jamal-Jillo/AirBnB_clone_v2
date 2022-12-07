#!/usr/bin/python3
"""State Module for AirBnB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """State class that describes a state."""

    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities
