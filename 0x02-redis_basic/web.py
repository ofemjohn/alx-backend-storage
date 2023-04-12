#!/usr/bin/env python3
'''Implementing an expiring web cache and tracker'''

import redis
from functools import wraps
from typing import Callable
import requests
redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    '''counting requests'''
    @wraps(method)
    def wrapper(url):
        '''decorator wrapper'''
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    '''return html'''
    req = requests.get(url)
    return req.text
