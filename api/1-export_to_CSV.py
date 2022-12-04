#!/usr/bin/python3
"""employee IDreturns information about his/her TODO list progress."""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    employee = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(employee)).json()
    TODO = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employee)).json()
    task_done = []
    for task in TODO:
        if task.get('completed') is True:
            task_done.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(task_done), len(TODO)))
    for done in task_done:
        print("\t {}".format(done))

with open('{}.csv'.format(employee), 'w') as csvfile:
    DATA = csv.writer(csvfile)
    for task in TODO:
        if task.get('completed'):
            DATA.writerow([employee, user.get('username'),
                            task.get('completed'), task.get('title')])
