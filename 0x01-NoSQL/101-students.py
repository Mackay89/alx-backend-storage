#!/usr/bin/env python3
"""Module containing script that returns students sorted by average score."""
import pymongo

def top_students(mongo_collection):
    """Function that returns all students sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        pymongo.command_cursor.CommandCursor: A cursor to the sorted list of students.
    """
    return mongo_collection.aggregate([
        {"$unwind": "$topics"},  # Deconstruct the array field
        {"$group": {
            "_id": "$name",  # Group by student name
            "averageScore": {"$avg": "$topics.score"}  # Calculate average score
        }},
        {"$sort": {"averageScore": -1}}  # Sort by average score in descending order
    ])

