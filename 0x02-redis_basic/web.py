#!/usr/bin/env python3
"""
Main file for demonstrating the usage of the Cache class from the exercise module.
"""
import redis
from exercise import Cache

def main() -> None:
    """
    Demonstrates storing data in Redis using the Cache class and retrieving it.
    """
    # Initialize the Cache class
    cache = Cache()

    # Define the data to be stored
    data: bytes = b"hello"

    # Store the data and get the key
    key: str = cache.store(data)
    print(f"Stored data under key: {key}")

    # Initialize local Redis instance
    local_redis = redis.Redis()

    # Retrieve and print the stored data
    stored_data = local_redis.get(key)
    if stored_data:
        print(f"Retrieved data: {stored_data.decode('utf-8')}")
    else:
        print("No data found for the given key.")

if __name__ == "__main__":
    main()

