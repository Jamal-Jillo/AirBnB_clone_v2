#!/usr/bin/python3
"""Review Module for AirBnB project."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that describes a review."""

    place_id = ""  # it will be the Place.id
    user_id = ""
    text = ""
