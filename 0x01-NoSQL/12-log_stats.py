#!/usr/bin/env python3
""" Script to display log statistics from a MongoDB collection """

from pymongo import MongoClient
from collections import Counter

def log_stats():
    """ Function to print log statistics from MongoDB """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count methods
    methods = collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ])
    
    print("Methods:")
    for method in methods:
        print(f"    method {method['_id']}: {method['count']}")

    # Count status
    status_count = collection.aggregate([
        {"$group": {"_id": "$status", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ])

    print(f"{total_logs} status check")
    for status in status_count:
        print(f"    status {status['_id']}: {status['count']}")

    # Count IPs
    ip_counts = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in ip_counts:
        print(f"    {ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
)

