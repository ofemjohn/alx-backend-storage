#!/usr/bin/env python3
import redis
import json
import uuid
from typing import Union
'''
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private
variable named _redis (using redis.Redis()) and
flush the instance using flushdb.
'''


class Cache:
    '''init method for Cache class'''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, float, int, bytes]) -> str:
        '''store data in cache with specified parameters'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
