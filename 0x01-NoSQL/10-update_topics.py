#!/usr/bin/env python3
"""Module containing function that updates topics of school docs based on name."""

from pymongo.collection import Collection
from typing import List

def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """Function that updates the 'topics' field of documents with a given name.

    Args:
        mongo_collection (Collection): The MongoDB collection object.
        name (str): The name of the documents to update.
        topics (List[str]): The new list of topics to set.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

