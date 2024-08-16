#!/usr/bin/env python3
"""
List all documents in a MongoDB collection
"""

from pymongo.collection import Collection
from typing import List, Dict, Any

def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
    List all documents in a given MongoDB collection.

    Args:
        mongo_collection (Collection): The MongoDB collection object from which documents will be retrieved.

    Returns:
        List[Dict[str, Any]]: A list of documents, where each document is represented as a dictionary.
    """
    if mongo_collection is None:
        return []
    documents = mongo_collection.find()
    return [doc for doc in documents]

