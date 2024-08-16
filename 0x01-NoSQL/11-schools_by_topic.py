#!/usr/bin/env python3
"""Module containing function that returns the list of schools with a specific topic."""

from pymongo.collection import Collection
from typing import List, Dict

def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict]:
    """Function that returns a list of schools with a specific topic.

    Args:
        mongo_collection (Collection): The MongoDB collection object.
        topic (str): The topic to search for in the documents.

    Returns:
        List[Dict]: A list of documents (schools) that contain the specified topic.
    """
    cursor = mongo_collection.find({"topics": topic})
    return list(cursor)

