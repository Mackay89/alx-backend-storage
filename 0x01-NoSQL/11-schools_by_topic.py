#!/usr/bin/env python3
""" 11-schools_by_topic """

from pymongo.collection import Collection
from typing import List, Dict

def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict]:
    """Returns a list of schools having a specific topic.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List[Dict]: A list of documents (schools) where the specified topic is present.
    """
    return list(mongo_collection.find({"topics": topic}))

