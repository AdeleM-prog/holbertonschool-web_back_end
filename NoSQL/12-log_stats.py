#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    counting = collection.count_documents({})
    print(f'{counting} logs')
    method_get = collection.count_documents({"method": "GET"})
    method_post = collection.count_documents({"method": "POST"})
    method_put = collection.count_documents({"method": "PUT"})
    method_patch = collection.count_documents({"method": "PATCH"})
    method_delete = collection.count_documents({"method": "DELETE"})

    print("Methods:")
    print(f"\tmethod GET: {method_get}")
    print(f"\tmethod POST: {method_post}")
    print(f"\tmethod PUT: {method_put}")
    print(f"\tmethod PATCH: {method_patch}")
    print(f"\tmethod DELETE: {method_delete}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
