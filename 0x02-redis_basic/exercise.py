#!/usr/bin/env python3
"""
Module that defines the Cache class for interacting with Redis.
"""
import redis
import uuid
from typing import Callable, Optional, TypeVar, Any

# Define type variables for function return types
T = TypeVar('T')

class Cache:
    """
    A class to interact with Redis, allowing storage, retrieval, and tracking of data.
    """
    def __init__(self) -> None:
        """
        Initialize the Cache instance, set up Redis client, and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
        Store the data in Redis and return the key.
        
        Args:
            data (Any): The data to store, which can be str, bytes, int, or float.
        
        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None) -> Optional[T]:
        """
        Retrieve the data associated with the key from Redis and apply a conversion function if provided.
        
        Args:
            key (str): The key to retrieve.
            fn (Optional[Callable[[bytes], T]]): An optional function to convert the data.
        
        Returns:
            Optional[T]: The converted data or None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve and convert the data associated with the key to a string.
        
        Args:
            key (str): The key to retrieve.
        
        Returns:
            Optional[str]: The string representation of the data or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve and convert the data associated with the key to an integer.
        
        Args:
            key (str): The key to retrieve.
        
        Returns:
            Optional[int]: The integer representation of the data or None if the key does not exist.
        """
        return self.get(key, lambda d: int(d))

def count_calls(method: Callable) -> Callable:
    """
    A decorator to count how many times a method is called.
    
    Args:
        method (Callable): The method to decorate.
    
    Returns:
        Callable: The decorated method.
    """
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Wrapper function that increments the count and calls the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    A decorator to record the history of inputs and outputs of a method.
    
    Args:
        method (Callable): The method to decorate.
    
    Returns:
        Callable: The decorated method.
    """
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Wrapper function that logs inputs and outputs and calls the original method.
        """
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", result)
        return result
    
    return wrapper

def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular method.
    
    Args:
        method (Callable): The method whose history is to be replayed.
    """
    key = method.__qualname__
    inputs = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)
    
    print(f"{key} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{key}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")

