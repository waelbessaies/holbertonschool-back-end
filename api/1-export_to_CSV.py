#!/usr/bin/python3
'''
A script to export data in the CSV format.
'''
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

with open('{}.csv'.format(employee), "w") as csvfile:
    DATA = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for task in TODO:
        DATA.writerow([employee, user.get('username'),
                      task.get('completed'), task.get('title')])
