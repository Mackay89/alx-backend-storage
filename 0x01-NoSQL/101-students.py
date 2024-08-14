def top_students(mongo_collection):
    """
    Return all students sorted by average score.
    
    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object for the students.
    
    Returns:
    List[dict]: A list of students, each with their _id, name, and averageScore, sorted by averageScore.
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    
    return list(mongo_collection.aggregate(pipeline))

