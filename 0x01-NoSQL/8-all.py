#!/usr/bin/env python3
""" 8-all """

from typing import List, Dict
from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> List[Dict]:
    """ Lists all documents in a collection """
    return list(mongo_collection.find())

