#!/usr/bin/env python3
''' 
Python function that changes all
topics of a school document based on the name:
'''


def update_topics(mongo_collection, name, topics):
    '''use name to change topics of the school documents'''
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
