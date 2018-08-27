#!/usr/bin/python3
'''
gathers information about an employee by ID and returns their TODO progress
'''
import json
import os
import requests


def main(argv):

    emp = requests.get('https://jsonplaceholder.typicode.com/users')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()
    users = {}
    final = {}
    filename = "todo_all_employees.json"

    for item in emp.json():
        users[item['id']] = item['username']

    with open(filename, 'w+') as f:
        for user in users:
            res = []
            for task in tasks:
                if task['userId'] == int(user):
                    copy = task.copy()
                    del copy['userId']
                    del copy['id']
                    username = users[user]
                    copy['username'] = username
                    res.append(copy)
            final[user] = res
        json.dump(final, f)


if __name__ == "__main__":
    import json
    import sys
    main(sys.argv)
