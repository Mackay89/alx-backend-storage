#!/usr/bin/env python3
""" 10-update_topics """

from pymongo.collection import Collection
from typing import List

def update_topics(mongo_collection: Collection, name: str, topics: List[str]):
    """Updates the topics of a school document based on the name.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        name (str): The name of the school to update.
        topics (List[str]): The list of topics to update in the school document.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

