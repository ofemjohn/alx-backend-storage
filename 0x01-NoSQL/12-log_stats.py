#!/usr/bin/env python3
'''
Python script that provides some stats
 about Nginx logs stored in MongoDB:'''
from pymongo import MongoClient

if __name__ == "__main__":
    '''retrun a state about nginx logs'''
    clientCollection = MongoClient('mongodb://127.0.0.1:27017')
    nginxCollection = clientCollection.logs.nginx

    logNumber = nginxCollection.count_documents({})
    print(f'{logNumber} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginxCollection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginxCollection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')
