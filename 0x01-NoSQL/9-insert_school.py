#!/usr/bin/env python3
'''
Python function that inserts a new 
document in a collection based on kwargs:
'''


def insert_school(mongo_collection, **kwargs):
    '''use kwargs to insert to a collection'''
    return mongo_collection.insert(kwargs)
