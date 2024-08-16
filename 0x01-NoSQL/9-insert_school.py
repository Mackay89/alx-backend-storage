#!/usr/bin/env python3
""" Script that inserts a document into a given MongoDB collection
    and returns the ID of the inserted document """

from pymongo.collection import Collection
from typing import Any, Dict

def insert_school(mongo_collection: Collection, **kwargs: Any) -> str:
    """Insert a document into the MongoDB collection and return the document ID.

    Args:
        mongo_collection (Collection): The MongoDB collection object where the document will be inserted.
        **kwargs: The attributes of the document to be inserted.

    Returns:
        str: The ID of the inserted document.
    """
    # Insert the document and retrieve the inserted ID
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)

