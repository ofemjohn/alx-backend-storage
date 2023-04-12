#!/usr/bin/env python3
import redis
import json
import uuid
from typing import Union, Callable, Optional
from functools import wraps
'''
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private
variable named _redis (using redis.Redis()) and
flush the instance using flushdb.
'''


def count_calls(method: Callable) -> Callable:
    '''
        Counts the number of times a method is called.
    '''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
            Wrapper function.
        '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and
    outputs for a particular function.
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    '''
    Args:
        method: The function to be decorated
    Returns:
        None
    '''
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    '''init method for Cache class'''
    def __init__(self):
        '''init method for cache class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, float, int, bytes]) -> str:
        '''store data in cache with specified parameters'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''return data from the cache.'''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''return string cache.'''
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        '''return int from cache.'''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
