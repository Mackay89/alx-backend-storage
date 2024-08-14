#!/usr/bin/env python3
"""
Module to fetch and cache web page content.
"""

import requests
import redis
import hashlib
import time
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()

def cache_page_expiration(func: Callable) -> Callable:
    """
    Decorator to cache function results with an expiration time.
    """
    def wrapper(url: str) -> str:
        # Generate a cache key based on the URL
        key = f"cache:{hashlib.sha256(url.encode()).hexdigest()}"
        cached_content = redis_client.get(key)

        if cached_content:
            return cached_content.decode('utf-8')

        # Call the actual function if not cached
        content = func(url)
        
        # Cache the result with an expiration time of 10 seconds
        redis_client.setex(key, 10, content)
        return content

    return wrapper

def count_url_accesses(func: Callable) -> Callable:
    """
    Decorator to count accesses to a URL.
    """
    def wrapper(url: str) -> str:
        # Increment the access count for the URL
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        
        return func(url)

    return wrapper

@cache_page_expiration
@count_url_accesses
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and returns it.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))

