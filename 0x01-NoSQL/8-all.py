<<<<<<< HEAD
=======
#!/usr/bin/env python3
""" 8-all """

>>>>>>> 37f399e42c40c1255d329e7bf2d6491eded764ec
from typing import List, Dict
from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> List[Dict]:
<<<<<<< HEAD
    """
    List all documents in a collection.
    
    :param mongo_collection: The pymongo collection object.
    :return: A list of documents. Returns an empty list if no document is found.
    """
    return list(mongo_collection.find())
=======
    """Lists all documents in a collection.
    
    Args:
        mongo_collection (Collection): The pymongo collection object.
        
    Returns:
        List[Dict]: A list of documents in the collection. Returns an empty list if no documents are found.
    """
    try:
        return list(mongo_collection.find())
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

>>>>>>> 37f399e42c40c1255d329e7bf2d6491eded764ec
