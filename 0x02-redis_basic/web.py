#!/usr/bin/env python3
"""
This module provides functionality to fetch and cache HTML content from a URL.
"""
import redis
import requests
import uuid
from typing import Callable
from functools import wraps

# Configure Redis client
r = redis.Redis()

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        key = f"count:{method.__qualname__}"
        r.incr(key)
        return method(*args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to record function input and output history.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        key_inputs = f"{method.__qualname__}:inputs"
        key_outputs = f"{method.__qualname__}:outputs"
        r.rpush(key_inputs, str(args))
        result = method(*args, **kwargs)
        r.rpush(key_outputs, result)
        return result
    return wrapper

def replay(method: Callable) -> None:
    """
    Replay the history of function calls.
    """
    key_inputs = f"{method.__qualname__}:inputs"
    key_outputs = f"{method.__qualname__}:outputs"
    inputs = r.lrange(key_inputs, 0, -1)
    outputs = r.lrange(key_outputs, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}{inp.decode()} -> {out.decode()}")

@count_calls
@call_history
def get_page(url: str) -> str:
    """
    Fetch HTML content from a URL, cache the result with an expiration time, and track access count.
    """
    cache_key = f"cache:{url}"
    count_key = f"count:{url}"

    # Check if the page is cached
    cached_content = r.get(cache_key)
    if cached_content:
        print("Cache hit")
        return cached_content.decode('utf-8')

    print("Cache miss")
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return ""

    # Cache the content with expiration time
    r.setex(cache_key, 10, content)
    r.incr(count_key)
    return content

if __name__ == "__main__":
    url = "http://httpbin.org/get"  # Use a valid URL
    print(get_page(url))

