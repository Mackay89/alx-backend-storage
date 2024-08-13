#!/usr/bin/env python3
""" 102-log_stats.py """

from pymongo import MongoClient

def print_nginx_stats(mongo_collection):
    # Count total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Aggregate method counts
    methods = mongo_collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ])
    
    print("Methods:")
    methods_count = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    for method in methods:
        methods_count[method["_id"]] = method["count"]
    
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {method}:\t{methods_count[method]}")

    # Aggregate status checks count
    status_checks = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

    # Aggregate IP counts
    ip_counts = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    
    print("IPs:")
    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_stats(nginx_collection)

