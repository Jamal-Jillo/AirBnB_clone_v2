"""Creates a package for the models module."""
from models.engine.file_storage import FileStorage
"""This module contains the storage instance."""
storage = FileStorage()
storage.reload()
