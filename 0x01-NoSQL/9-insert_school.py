#!/usr/bin/env python3
""" 9-insert_school """

from pymongo.collection import Collection

def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """Inserts a new document in the collection.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        **kwargs: Key-value pairs to be included in the new document.
    
    Returns:
        str: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)

