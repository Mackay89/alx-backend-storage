#!/usr/bin/env python3
"""Module containing script that returns students sorted by average score."""
import pymongo
from pymongo.collection import Collection
from typing import List, Dict, Any

def top_students(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """Function that returns all students sorted by average score.

    Args:
        mongo_collection (Collection): The MongoDB collection object.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries with student names and their average scores.
    """
    cursor = mongo_collection.aggregate([
        {"$unwind": "$topics"},  # Deconstruct the array field
        {"$group": {
            "_id": "$name",  # Group by student name
            "averageScore": {"$avg": "$topics.score"}  # Calculate average score
        }},
        {"$sort": {"averageScore": -1}}  # Sort by average score in descending order
    ])
    
    # Convert cursor to a list of dictionaries
    return list(cursor)

