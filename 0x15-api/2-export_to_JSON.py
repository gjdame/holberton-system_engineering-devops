#!/usr/bin/python3
'''
gathers information about an employee by ID and returns their TODO progress
'''
import json
import os
import requests
import sys

def main(argv):
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    name = emp.json().get('username')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()
    res = []
    final = {}
    filename = sys.argv[1] + ".json"

    with open(filename, 'w+') as f:
        for task in tasks:
            if task['userId'] == int(sys.argv[1]):
                res.append(task)
        final[sys.argv[1]] = res
        json.dump(final, f)


if __name__ == "__main__":
    import json
    import sys
    main(sys.argv)
