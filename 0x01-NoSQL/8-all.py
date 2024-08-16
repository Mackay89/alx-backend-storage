#!/usr/bin/env python3
"""
List all documents in a MongoDB collection.
"""
import pymongo
from pymongo.collection import Collection
from typing import List, Dict, Any

def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
    Function to list all documents in a collection.

    Args:
        mongo_collection (Collection): The MongoDB collection object.

    Returns:
        List[Dict[str, Any]]: A list of documents in the collection.
    """
    # Check if mongo_collection is None (not implemented for collections)
    if mongo_collection is None:
        return []

    # Fetch all documents from the collection
    documents = mongo_collection.find()
    # Convert cursor to a list of dictionaries
    return list(documents)

