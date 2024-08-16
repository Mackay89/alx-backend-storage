#!/usr/bin/env python3
"""Module containing a function to return HTML content of a particular URL with caching."""

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize the Redis connection
data = redis.Redis(host='localhost', port=6379, db=0)

def cached_content_fun(method: Callable[[str], str]) -> Callable[[str], str]:
    """Decorator to cache the content of a URL."""

    @wraps(method)
    def wrapper(url: str) -> str:
        cached_content = data.get(f"cached:{url}")
        if cached_content:
            return cached_content.decode('utf-8')

        content = method(url)
        data.setex(f"cached:{url}", 10, content)
        return content

    return wrapper

@cached_content_fun
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL and tracks access count."""

    try:
        # Increment the count for the URL
        count = data.incr(f"count:{url}")
        
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        content = response.text

        # Optionally print debug information
        # print(content)
        # print(f"Count: {count}")

        return content

    except requests.RequestException as e:
        # Handle exceptions for network errors or invalid responses
        print(f"Error fetching URL: {e}")
        return ""

# Example usage
if __name__ == "__main__":
    # Fetch and print content of URLs
    print(get_page('http://slowwly.robertomurray.co.uk'))
    print(get_page('http://google.com'))

