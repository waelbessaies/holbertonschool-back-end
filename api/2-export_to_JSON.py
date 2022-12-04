#!/usr/bin/python3
"""
export to json
"""
import json
import requests
import sys


if __name__ == '__main__':
    employee = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee)).json()
    TODO = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(sys.argv[1])).json()

    with open("{}.json".format(employee), "w") as filejson:
        json.dump({employee: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in TODO]}, filejson)
