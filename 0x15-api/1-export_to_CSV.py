#!/usr/bin/python3
'''
gathers information about an employee by ID and returns their TODO progress
'''
import csv
import os
import requests
import sys


def main(argv):

    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(sys.argv[1]))
    name = emp.json().get('username')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()
    complete = 0
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    titles = []
    total = 0
    filename = sys.argv[1] + ".csv"
    with open(filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, quotechar='"')
        for task in tasks:
            if task['userId'] == int(sys.argv[1]):
                task['name'] = name
                writer.writerow([task['userId'], task['name'],
                                 task['completed'], task['title']])


if __name__ == "__main__":
    import sys
    main(sys.argv)
