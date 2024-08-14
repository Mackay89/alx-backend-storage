from typing import List, Dict
from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    List all documents in a collection.
    
    :param mongo_collection: The pymongo collection object.
    :return: A list of documents. Returns an empty list if no document is found.
    """
    return list(mongo_collection.find())
